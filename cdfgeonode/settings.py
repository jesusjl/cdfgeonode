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


MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
# ...
'debug_toolbar.middleware.DebugToolbarMiddleware',
# ...
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
'debug_toolbar',
'south',
)


TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (

    "sekizai.context_processors.sekizai",
)
