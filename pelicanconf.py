#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Grupo de Usuários Python do Paraná'
SITENAME = 'GruPy-PR'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

LOCALE = 'pt_BR.UTF-8'
DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('GruPy-PR no Telegram', 'https://t.me/python_pr'),
        ('GruPy-PR no MeetUp', 'http://www.meetup.com/pt/GruPy-PR/'),
        ('GruPy-PR no Google Groups',
         'https://groups.google.com/forum/#!forum/grupy-pr'),
        ('Grupy-PR no Github', 'https://github.com/grupypr'),
        ('PythonBrasil', 'http://www.pythonbrasil.com.br/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/favicon.ico', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
ARTICLE_URL = '{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
DEFAULT_DATE_FORMAT = ('%d de %B de %Y')

# THEME CONFIGS
THEME = 'themes/medius'
DEFAULT_COVER = 'https://placeimg.com/1920/800/nature'
DEFAULT_PROFILE_IMG = '/images/thumbnail/profile.png'
DEFAULT_CATEGORY_THUMB = '/images/thumbnail/grupypr-thumb.png'
DISPLAY_CATEGORIES_ON_MENU = False

"""
Para criar um novo autor, altere esse dicionario com as informações do
novo autor:
    'Nome do Autor': {
        'image': 'full path da imagem do autor. Tamanho recomendado 200x200 (opcional)',
        'cover': 'imagem de fundo da página do autor. Tamanho recomendado 1920x800 (opcional)',
        'links': (uma lista de tuplas com ("nome do icone", "link")),
    }
"""
MEDIUS_AUTHORS = {
    'Álvaro Justen': {
        'image': 'https://avatars3.githubusercontent.com/u/186126?v=3&s=150',
        'links': (
            ('github-square', 'https://github.com/turicas'),
            ('twitter-square', 'https://twitter.com/turicas'),
        )
    },
    'Thiago Serafim': {
        'image': 'https://avatars3.githubusercontent.com/u/7226969?v=3&s=460',
        'links': (
            ('github-square', 'https://github.com/tserafim'),
            ('twitter-square', 'https://twitter.com/thiagoserafim'),
        )
    },
    'William Souza': {
        'image': 'https://avatars3.githubusercontent.com/u/215986?v=3&s=150',
        'links': (
            ('github-square', 'https://github.com/wiliamsouza'),
        )
    },
    'Ellison Leão': {
        'image': 'https://avatars3.githubusercontent.com/u/178641?v=3&s=150',
        'links': (
            ('github-square', 'https://github.com/ellisonleao'),
            ('twitter-square', 'https://twitter.com/ellisonleao'),
        )
    },
    'Ramiro Batista da Luz': {
        'image': 'https://avatars3.githubusercontent.com/u/293174?v=4&s=150',
        'links': (
            ('github-square', 'https://github.com/ramiroluz'),
            ('twitter-square', 'https://twitter.com/ramiroluz'),
        )
    },
}

"""
Configurações para página de categorias
formato:
'nome categoria': {
  'description': 'uma descrição',
  'thumbnail': 'path para imagem thumb. Tamanho 100x100', (opcional)
}
"""
MEDIUS_CATEGORIES = {
    'Encontros': {
        'description': 'Post-mortem dos nossos encontros',
    }
}

PLUGINS = ['plugins.meetup']

MEETUP_API_KEY = '3150302e2be87c4cf19651b7f26'
MEETUP_GROUP_URLNAME = 'grupy-pr'
