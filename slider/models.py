from django.db import models
from django.utils.translation import get_language

from filer.fields.image import FilerImageField

class Slide(models.Model):
    title = models.CharField(max_length=100)
    image = FilerImageField(help_text="For best result, use an image not smaller than 952x317")
    caption = models.CharField(max_length=400, blank=True)
    caption_es = models.CharField(max_length=400, blank=True)
    link = models.CharField(max_length=100, blank=True)
    sort_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order', 'title']

    def caption_translated(self):
        if get_language() == 'es' and len(self.caption_es) > 0:
            return self.caption_es
        else:
            return self.caption

    def __unicode__(self):
        return self.title
