#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from distutils.sysconfig import get_python_lib

AUTHOR = 'Mark Korondi'
SITENAME = "Mark's space"
SITEURL = 'http://localhost:9999'

PATH = 'content'

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('linkedin', 'https://linkedin.com/in/markkorondi'),
    ('github', 'https://github.com/kmarc'),
    ('compass', 'https://www.polarsteps.com/MarkKorondi/'),
    ('twitter', 'https://twitter.com/kmarc'),
    ('facebook', 'https://facebook.com/markkorondi'),
    ('key', 'https://keybase.io/kmarc#show-public'),
)

DEFAULT_PAGINATION = False

THEME = 'themes/MinimalXY'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

ARTICLE_SAVE_AS = 'posts/{date:%Y-%m-%d}-{slug}.html'
ARTICLE_URL = 'posts/{date:%Y-%m-%d}-{slug}.html'

WITH_FUTURE_DATES = True

PORT = 9999

TWITTER_USERNAME = 'kmarc'

from datetime import date
MINIMALXY_CURRENT_YEAR = date.today().year
AUTHOR_AVATAR = 'https://s.gravatar.com/avatar/3a946793d2adc7d1dc9b8a2a749f1401?s=240'
AUTHOR_INTRO = u'Software developer. Traveler. Minimalist.'
AUTHOR_DESCRIPTION = AUTHOR_INTRO

WITH_FUTURE_DATES = True

PLUGIN_PATHS = [get_python_lib(), "../../getpelican/pelican-plugins/",]

STATIC_PATHS = ['extra/keybase.txt']
EXTRA_PATH_METADATA = {'extra/keybase.txt': {'path': 'keybase.txt'}}
