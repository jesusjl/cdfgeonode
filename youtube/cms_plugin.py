from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from youtube.models import VideoPlugin as VideoPluginModel

class YoutubePlugin(CMSPluginBase):
    model = VideoPluginModel
    name = _("Youtube")
    render_template = "youtube.html"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(YoutubePlugin)
