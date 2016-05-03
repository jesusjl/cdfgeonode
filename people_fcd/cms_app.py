from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PeopleApp(CMSApp):
    name = _("People App") # give your app a name, this is required
    urls = ["people_fcd.urls"] # link your app to url configuration(s)

apphook_pool.register(PeopleApp) # register your app
