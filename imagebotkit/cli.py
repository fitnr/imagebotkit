#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of imagebot.
# https://github.com/fitnr/imagebotkitkit

# Licensed under the MIT license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, imagebot <fitnr@fakeisthenewreal>

import argparse
import twitter_bot_utils as tbu
from . import imagebotkit

def main():
    parent = tbu.args.parent()
    parser = argparse.ArgumentParser('imagebot', parents=(parent,))

    parser.add_argument('user', type=str)
    parser.add_argument('file', nargs='*', help='file or directory glob to search for images to post')
    parser.add_argument('-r', '--record', type=str, help='text file with list of files to not post. Posted images will be added')
    parser.add_argument('-C', '--count', type=int, choices=(1, 2, 3, 4), default=1, help='number of images to post (default: 1)')
    parser.add_argument('--status', type=str, help='tweet text')

    args = parser.parse_args()

    image_paths = imagebotkit.pick_image(args.file, args.count, args.record)

    api_args = ['key', 'secret', 'consumer_key', 'consumer_secret']

    kwargs = {k: getattr(args, k) for k in api_args if getattr(args, k, None)}

    if not args.dry_run:
        twitter = tbu.api.API(args.user, config=args.config_file, **kwargs)

        media_strings = imagebotkit.post_images(twitter, image_paths)

        twitter.update_status(status=args.status, media_ids=media_strings)

        imagebotkit.update_record(image_paths, args.record)


if __name__ == '__main__':
    main()
