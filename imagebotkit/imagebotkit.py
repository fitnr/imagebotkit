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
    '.jpeg',
    '.gif',
    '.png',
    '.webp'
)

try:
    basestring
except NameError:
    basestring = str

def valid_image(filename):
    return os.path.splitext(filename)[1] in VALID_IMAGE_EXTS

def past_posts(record):
    past_images = set()
    if record and os.path.exists(record):
        with open(record) as f:
            past_images = set(x.strip() for x in f.readlines())

    return past_images


def pick_image(fileglobs, count=None, record=None):
    '''
    :fileglobs list paths or globs
    :count int Number of paths to return. Default: 1
    :record str Name of file containing paths to exclude
    '''
    count = count or 1

    past_images = past_posts(record)
    prospectives = set()
    if isinstance(fileglobs, basestring):
        fileglobs = (fileglobs,)

    for globule in fileglobs:
        globule = os.path.expandvars(os.path.expanduser(globule))

        if os.path.isfile(globule):
            prospectives.update([globule])

        else:
            for path in glob(globule):
                for dirpath, _, files in walk(path):
                    images = (os.path.join(dirpath, fn) for fn in files if valid_image(fn))
                    prospectives.update(images)

    prospectives = prospectives.difference(past_images)

    possibles = sorted(list(prospectives), key=lambda _: random())

    return possibles[0:count]

def post_images(api, paths):
    media_ids = []

    for path in paths:
        try:
            media = api.media_upload(path)
            print(media)
        except TweepError:
            raise

        media_ids.append(media.media_id_string)

    return media_ids

def update_record(image_paths, record):
    with open(record, 'a') as f:
        f.writelines((i + linesep for i in image_paths))
