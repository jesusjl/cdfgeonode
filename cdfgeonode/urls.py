from django.conf.urls import patterns, url
from geonode.urls import *
# from django.conf.urls.i18n import i18n_patterns

from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern

# urlpatterns +=  i18n_patterns('',
urlpatterns +=  patterns('',
    # Static pages
#    url(r'^$', 'polls.views.index', name='index'),
     url(r'^demo/$', 'demo.views.index'),
	(r'^notifications/', get_nyt_pattern()),
    #  url(r'^/$',TemplateView.as_view(template_name='base.html'),name='home'),
	(r'^wiki/_accounts/sign-up/$','demo.views.index'),
    (r'^wiki/', get_wiki_pattern()),
    url(r'^',  include('cms.urls')),

 )


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
