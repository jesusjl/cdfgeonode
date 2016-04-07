from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class AmazonWidgetPlugin(CMSPluginBase):
    model = CMSPlugin
    name = "Amazon Widget"
    render_template = "amazon_widget.html"

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(AmazonWidgetPlugin)
