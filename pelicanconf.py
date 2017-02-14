#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Grupo de Usuários Python do Paraná'
SITENAME = 'GruPy-PR'
SITEURL = 'http://localhost:8000'

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
        ('GruPy-PR no Google Groups',
         'https://groups.google.com/forum/#!forum/grupy-pr'),
        ('PythonBrasil', 'http://www.pythonbrasil.com.br/'),
        ('Github', 'https://github.com/grupypr'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images']
ARTICLE_URL = '{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'


# THEME CONFIGS
THEME = 'themes/medius'
DEFAULT_COVER = 'http://lorempixel.com/1920/800/abstract/'

# Para criar um novo autor, altere esse dicionario com as informações do
# novo autor
# image - full path da imagem do autor. Tamanho recomendado 200x200
# cover - imagem de fundo da página do autor. Tamanho recomendado 1920x800
# links - uma lista de tuplas com ("nome do icone", "link")
MEDIUS_AUTHORS = {
    'Álvaro Justen': {
        'image': 'https://avatars3.githubusercontent.com/u/186126?v=3&s=150',
        'cover': DEFAULT_COVER,
        'links': (
            ('github', 'https://github.com/turicas'),
            ('twitter-square', 'https://twitter.com/turicas'),
        )
    },
}
