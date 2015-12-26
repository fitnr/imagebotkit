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
    parser = argparse.ArgumentParser('imagebot', usage='%(prog)s [options] screen_name path [path ...]', parents=(parent,))

    parser.add_argument('screen_name', type=str, help='Twitter user')
    parser.add_argument('path', nargs='+', help='files, or directories to scan for images')
    parser.add_argument('-r', '--record', type=str, help='text file with list of files to not post. Posted images will be added')
    parser.add_argument('-C', '--count', type=int, choices=(1, 2, 3, 4), default=1, help='number of images to post (default: 1)')
    parser.add_argument('--status', type=str, default=' ', help='tweet text')

    args = parser.parse_args()

    logger = tbu.args.add_logger(args.screen_name, args.verbose)
    logger.debug('imagebotkit: starting with %s', args.screen_name)

    image_paths = imagebotkit.pick_image(args.path, args.count, args.record)
    logger.debug('imagebotkit: got images %s', image_paths)

    api_args = ['key', 'secret', 'consumer_key', 'consumer_secret']

    kwargs = {k: getattr(args, k) for k in api_args if getattr(args, k, None)}

    if not args.dry_run:
        twitter = tbu.api.API(args.screen_name, config=args.config_file, **kwargs)

        media_strings = imagebotkit.post_images(twitter, image_paths)

        twitter.update_status(status=args.status, media_ids=media_strings)

        imagebotkit.update_record(image_paths, args.record)


if __name__ == '__main__':
    main()
