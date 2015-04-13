from django.conf.urls import patterns, url

from geonode.urls import *

urlpatterns = patterns('',

    # Static pages
#    url(r'^$', 'polls.views.index', name='index'),
     url(r'^demo/$', 'demo.views.index'),
 ) + urlpatterns


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )