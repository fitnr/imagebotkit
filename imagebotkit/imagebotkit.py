#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of imagebot.
# https://github.com/fitnr/imagebotkitkit

# Licensed under the MIT license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, imagebot <fitnr@fakeisthenewreal>

import os.path
from os import linesep, walk
from glob import glob
from random import random
from tweepy.error import TweepError

VALID_IMAGE_EXTS = (
    '.jpg',
    '.gif',
    '.png',
    '.webp'
)

def valid_image(filename):
    return os.path.splitext(filename)[1] in VALID_IMAGE_EXTS

def pick_image(fileglobs, count=None, record=None):
    count = count or 1

    past_images = set()
    prospectives = set()

    if record and os.path.exists(record):
        with open(record) as f:
            past_images = set(x.trim() for x in f.readlines())

    for globule in fileglobs:
        globule = os.path.expandvars(os.path.expanduser(globule))
        for path in glob(globule):
            for dirpath, _, filenames in walk(path):
                prospectives.update(os.path.join(dirpath, fn) for fn in filenames if valid_image(fn))

    prospectives = prospectives.difference(past_images)

    possibles = sorted(list(prospectives), key=lambda _: random())

    return possibles[1:count]

def post_images(api, paths):
    media_ids = []

    for path in paths:
        try:
            media = api.media_upload(path)
        except TweepError:
            continue

        media_ids.append(media.media_id_string)

    return media_ids

def update_record(image_paths, record):
    with open(record, 'a') as f:
        for i in image_paths:
            f.write(i + linesep)
