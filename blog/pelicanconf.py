#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
AUTHOR = u'Mirad'
SITENAME = u'بلاگ میراد(هوشمند بخوانید!)'
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
GZIP_CACHE = True
GOOGLE_ANALYTICS = 'UA-52755705-2'
META_FA_KEYWORDS = u"mirad,میراد,بلاگ,وبلاگ,وبلاگ میراد,بلاگ میراد,نرم‌افزار میراد,اپلیکیشن,موبایل,نرم‌افزار موبایل میراد,اخبار,مقاله,مجله,ورزش,سیاسی,تکنولوژی,اقتصادی,روزنامه,نرم‌افزار,اندروید,خوراک,فید,خبرخوان,میراد,خبر شخصی,خبر هوشمن"
META_EN_KEYWORDS = u"rss,mirad,news,blog,mirad blog,weblog,aggregator, ios, iphone, application, mobile, android"
META_DESC = u"بلاگ میراد ‌|‌ در این بلاگ شما آخرین رویدادها و خبرهای مربوط به توسعه‌ی نرم افزار میراد را می‌خوانید."
META_SUBJECT = u"بلاگ میراد(آخرین خبر‌ها از توسعه‌ی میراد): هوشمند بخوانید!"