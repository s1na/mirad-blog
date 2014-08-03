#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
AUTHOR = u'Mirad'
SITENAME = u'وبلاگ | میراد'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = u'fa'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
THEME='miradTheme'
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["jalali"]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
