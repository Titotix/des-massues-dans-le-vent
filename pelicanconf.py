#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris & Thibault'
SITENAME = 'Des massues dans le vent'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = 'fr'

THEME = 'themes/notmyideacustom'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['photos']

# photos plugin conf
PHOTO_LIBRARY = 'content/images'
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (640, 480, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = False
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = 'Des massues dans le vent'

PHOTO_RESIZE_JOBS = 2
