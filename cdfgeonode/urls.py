from django.conf.urls import patterns, url

from geonode.urls import *

urlpatterns = patterns('',

    # Static pages
#    url(r'^$', 'polls.views.index', name='index'),
     url(r'^demo/$', 'demo.views.index'),
 ) + urlpatterns




