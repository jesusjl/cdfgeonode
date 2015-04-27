from django.conf.urls import patterns, url

from wiki.urls import get_pattern as get_wiki_pattern

from django_nyt.urls import get_pattern as get_nyt_pattern

from geonode.urls import *

urlpatterns = patterns('',

    # Static pages
#    url(r'^$', 'polls.views.index', name='index'),
     url(r'^demo/$', 'demo.views.index'),
     url(r'^notifications/', get_nyt_pattern()),
     url(r'^wiki/', get_wiki_pattern()),
 ) + urlpatterns


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

