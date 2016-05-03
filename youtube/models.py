from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin

def youtube_id(url):
    import urlparse
    urldata = urlparse.urlparse(url)
    querydata = urlparse.parse_qs(urldata.query)
    id = querydata['v'][0]
    return id

def get_video_info(youtube_id):
    ''' Retrieves info from Youtube API v3 '''
    import json
    import urllib2
    from django.conf import settings
    key = settings.YOUTUBE_API_V3_KEY
    api_url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=%s&key=%s" % (youtube_id, key)
    result = json.load(urllib2.urlopen(api_url))
    return result

class Video(models.Model):
    url = models.URLField()
    youtube_id = models.CharField(max_length=50, editable=False, default='')
    title = models.CharField(max_length=200, editable=True, default='', blank=True, help_text=_('Leave empty to use the original video title'))
    thumbnail = models.ImageField(upload_to='mistavideo', editable=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_embed_url(self):
        return 'http://www.youtube.com/embed/%s?autoplay=1' % self.youtube_id

    def save(self, *args, **kwargs):
        from django.core.files import File
        from django.core.files.temp import NamedTemporaryFile
        import urllib2
        from urlparse import urlparse

        self.youtube_id = youtube_id(self.url)
        video_info = get_video_info(self.youtube_id)
        if self.title == '':
            self.title = video_info['items'][0]['snippet']['title']


        image_url = video_info['items'][0]['snippet']['thumbnails']['high']['url']
        image_name = self.youtube_id + '.' + urlparse(image_url).path.split('.')[-1]
        img_file = NamedTemporaryFile(delete=True)
        img_file.write(urllib2.urlopen(image_url).read())
        img_file.flush()

        self.thumbnail.save(image_name, File(img_file), save=False)

        super(Video, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class VideoPlugin(CMSPlugin):
    video = models.ForeignKey(Video)

    def __unicode__(self):
        return self.video.title
