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

SITENAME = 'cdfgeonode'

MEDIA_ROOT = '/var/www/geonode/uploaded/'
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


from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)


# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

MIDDLEWARE_CLASSES = (
    #'cms.middleware.utils.ApphookReloadMiddleware', # django-cms 3.2
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',


    # The setting below makes it possible to serve different languages per
    # user depending on things like headers in HTTP requests.
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',


)


INSTALLED_APPS = INSTALLED_APPS + (
# ...
'django.contrib.sites', # django 1.6.2
'django.contrib.humanize',
'django_nyt',
'mptt',
'sekizai',
'sorl.thumbnail',
'wiki',
'wiki.plugins.attachments',
'wiki.plugins.notifications',
'wiki.plugins.images',
'wiki.plugins.macros',





'cms',  # django CMS itself
'treebeard',  # utilities for implementing a tree
'menus',  # helper for model independent hierarchical website navigation
'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
'reversion',
'djangocms_file',
'djangocms_flash',
'djangocms_googlemap',
'djangocms_inherit',
'djangocms_picture',
'djangocms_teaser',
'djangocms_video',
'djangocms_link',
'djangocms_text_ckeditor',
#'djangocms_snippet',


'debug_toolbar',
'south',
)


TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (

    "sekizai.context_processors.sekizai",
)


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



CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False
