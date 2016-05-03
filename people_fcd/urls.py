from django.conf.urls import *

urlpatterns = patterns('people_fcd.views',
    url(r'^(?P<group>\w+)/$', 'list', name='list'),
)
