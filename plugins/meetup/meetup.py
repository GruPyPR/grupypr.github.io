#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Meetup plugin
=============

This plugin generates a list of upcoming and past events for a specific meetup
group.
"""
from collections import namedtuple
from datetime import datetime

from pelican import signals
from tapioca_meetup import Meetup

import logging
log = logging.getLogger(__name__)


def generate_events(generator):
    generator.context['events_list'] = []
    try:
        key = generator.settings['MEETUP_API_KEY']
        group = generator.settings['MEETUP_GROUP_URLNAME']
    except KeyError:
        log.error('MEETUP_API_KEY and MEETUP_GROUP_URLNAME not passed.'
                  'Can\'t generate the events list')
        return

    api = Meetup(key=key)
    try:
        events = api.group_events(urlname=group).get()
    except Exception as e:
        log.exception('Error on getting information from Meetup API', e)
        return

    for event in events:
        # grabbing event dict data
        e = event().data
        # converting unixtime to datetime
        e['time'] = datetime.fromtimestamp(e['time'] / 1000)
        # adding event object into events_list context
        generator.context['events_list'].append(e)


def register():
    signals.article_generator_finalized.connect(generate_events)
