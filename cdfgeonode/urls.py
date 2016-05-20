from django.conf.urls import patterns, url
from django.conf.urls.i18n import i18n_patterns


from geonode.urls import *

from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern


urlpatterns += patterns('',

    # Static pages
#    url(r'^$', 'polls.views.index', name='index'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^demo/$', 'demo.views.index'),
    (r'^wiki/notifications/', get_nyt_pattern()),
    #url(r'^/?$', TemplateView.as_view(template_name='site_index.html'), name='home'),
	(r'^wiki/_accounts/sign-up/$','demo.views.index'),
    (r'^wiki/', get_wiki_pattern()),
    url(r'^shiny_apps/', include('cms_shiny.urls', namespace='cms_shiny')),

    url(r'^', include('cms.urls')),
    #url(r'^', include('djangocms_blog.urls')),
    url(r'^djangocms_blog/', include('djangocms_blog.urls', namespace='djangocms_blog')),
    url(r'^select2/', include('django_select2.urls')),
    (r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

 )


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
