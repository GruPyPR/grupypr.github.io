#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Grupo de Usuários Python do Paraná'
SITENAME = 'GruPy-PR'
#SITEURL = 'http://grupypr.github.io'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('GruPy-PR no Telegram', 'https://t.me/grupy_pr'),
        ('GruPy-PR no MeetUp', 'http://www.meetup.com/pt/GruPy-PR/'),
        ('GruPy-PR no Google Groups', 'https://groups.google.com/forum/#!forum/grupy-pr'),
        ('PythonBrasil', 'http://www.pythonbrasil.com.br/'),
)

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images']
ARTICLE_URL = '{date:%Y}/{slug}.html'
