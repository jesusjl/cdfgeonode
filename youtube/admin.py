from django.contrib import admin
from youtube.models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'youtube_id')

admin.site.register(Video, VideoAdmin)
