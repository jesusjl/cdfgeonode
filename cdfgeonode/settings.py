# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
from geonode.settings import *
from django.conf import settings as django_settings
#
# General Django development settings
#
gettext = lambda s: s

from django.utils.translation import ugettext



SITENAME = 'cdfgeonode'

# MEDIA_ROOT = '/var/www/geonode/uploaded/'
STATIC_ROOT = '/var/www/geonode/static/'

SITE_ID = 1

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "cdfgeonode.wsgi.application"


# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'cdfgeonode.urls'


MEDIA_ROOT = os.path.join(LOCAL_ROOT, 'media/')

MEDIA_URL = '/media/'

from django.utils.translation import ugettext_lazy as _



# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    )




INSTALLED_APPS = INSTALLED_APPS + (
# ...
'django.contrib.sites', # django 1.6.2
'django.contrib.humanize',
'django_nyt',
'mptt',
'treebeard',
'sekizai',
'sorl.thumbnail',
'wiki',
'wiki.plugins.attachments',
'wiki.plugins.notifications',
'wiki.plugins.images',
'wiki.plugins.macros',
'debug_toolbar',
'south',
)

DJANGO_CMS_INSTALLED_APPS = (

'djangocms_text_ckeditor',
'djangocms_style',
'djangocms_column',
'cms',  # django CMS itself
#'mptt',  # utilities for implementing a tree
'menus',  # helper for model independent hierarchical website navigation

#'south',  # Only needed for Django < 1.7
#'sekizai',  # for javascript and css management
#'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
'reversion',
'django.contrib.messages',  # to enable messages framework (see :ref:`Enable messages <enable-messages>`)

#django-filer
'cms_shiny',
'easy_thumbnails',
#'filer',
'mptt',

# cmsplugin-filer

'cmsplugin_filer_file',
'cmsplugin_filer_folder',
'cmsplugin_filer_link',
'cmsplugin_filer_image',
'cmsplugin_filer_teaser',
'cmsplugin_filer_video',

#djangocms-blog

'filer',
'easy_thumbnails',
#'cmsplugin_filer_image',
'aldryn_apphooks_config',
'parler',
'taggit',
'django_select2',
'taggit_autosuggest',
'meta',
# 'meta_mixin',
'djangocms_blog',
'admin_enhancer',

'smart_load_tag',
#custom
'slider',
'core',

)

INSTALLED_APPS += DJANGO_CMS_INSTALLED_APPS



# django-filer thumbnail

THUMBNAIL_HIGH_RESOLUTION = True

# djangocms-blog
#
SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
    'taggit': 'taggit.south_migrations',
}

META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

TIME_ZONE = 'Pacific/Galapagos'

LANGUAGE_CODE = 'en'


LANGUAGES = (
    ## Customize this
    ('en', gettext('English')),
    ('es', gettext('Spanish')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'public': True,
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'code': 'en',
            'hide_untranslated': False,
        },
        {
            'public': True,
            'name': gettext('es'),
            'redirect_on_fallback': True,
            'code': 'es',
            'hide_untranslated': False,
        },
    ],
    'default': {
        'public': True,
        'redirect_on_fallback': True,
        'hide_untranslated': False,
    },
}

PARLER_LANGUAGES = {
    1: (
        {'code': 'en',},
        {'code': 'es',},
    ),
}


AUTH_USER_MODEL = 'people.Profile'

# thumbnail

# For easy_thumbnails to support retina displays (recent MacBooks, iOS)
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_QUALITY = 95

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
THUMBNAIL_SUBDIR = 'versions'


# djangocms

CMS_TEMPLATES = (
    ('site_base.html', 'Homepage'),
    ('2-col-blog.html', 'Two Column Blog Template'),
    ('mapstories.html', 'Two Column MapStories Template'),
    ('1-col.html', 'One column template'),
    ('1-col-donate.html',
        'One Column Template customized for the Donate page'),
    ('djangocms_blog/post_list.html', 'Post List'),
    ('index.html', 'Geonode Homepage'),
    ('amazon.html', 'Amazon Template'),

)

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',

    # Add also the following modules if you're using these plugins:

    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    "django.core.context_processors.tz",
    'django.core.context_processors.media',
    "django.core.context_processors.static",
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'account.context_processors.account',
    # The context processor below adds things like SITEURL
    # and GEOSERVER_BASE_URL to all pages that use a RequestContext
    'geonode.context_processors.resource_urls',
    'geonode.geoserver.context_processors.geoserver_urls',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # The setting below makes it possible to serve different languages per
    # user depending on things like headers in HTTP requests.
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'pagination.middleware.PaginationMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # This middleware allows to print private layers for the users that have
    # the permissions to view them.
    # It sets temporary the involved layers as public before restoring the permissions.
    # Beware that for few seconds the involved layers are public there could be risks.
    # 'geonode.middleware.PrintProxyMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

)

BLOG_USE_PLACEHOLDER = True

#cmsplugin_filer_image provides integration with djangocms-text-ckeditor.
#Add this setting to enable it:

TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

# Non-configurable (at the moment)
APP_LABEL = 'wiki'
WIKI_LANGUAGE = 'markdown'

# The editor class to use -- maybe a 3rd party or your own...? You can always
# extend the built-in editor and customize it....
EDITOR = getattr(
    django_settings,
    'WIKI_EDITOR',
    'wiki.editors.markitup.MarkItUp')

MARKDOWN_KWARGS = {
    'extensions': [
        'footnotes',
        'attr_list',
        'extra',
        'codehilite',
        'sane_lists',
    ],
    'safe_mode': 'replace',
    'extension_configs': {
        'toc': {
            'title': _('Table of Contents')}},
}
MARKDOWN_KWARGS.update(getattr(django_settings, 'WIKI_MARKDOWN_KWARGS', {}))

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# ckeditor allow iframes

TEXT_ADDITIONAL_TAGS = ('iframe',)
TEXT_ADDITIONAL_ATTRIBUTES = ('scrolling', 'allowfullscreen', 'frameborder')
