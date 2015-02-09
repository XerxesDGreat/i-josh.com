#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josh Wickham'
SITENAME = u'i-Josh'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'silk-pajamas'

PLUGIN_PATHS =['plugins']
PLUGINS = ['panoviewer.panoviewer']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/XerxesDGreat'),
    ('facebook', 'https://facebook.com/josh.wickham'),
    ('github', 'https://github.com/XerxesDGreat'),
    ('steam-square', 'https://steamcommunity.com/id/xerxesdgreat/games/')
)

#WRITE_SELECTED = ('output/yosemite-panoramas.html',)



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# pelican-cait template options
USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (
    ('Family', 'category/family.html'),
    ('Photography', 'category/photography.html'),
    ('Projects', 'category/projects.html'),
    ('Thoughts', 'category/thoughts.html'),
)

STATIC_PATHS = ['panorama']
