#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of imagebot.
# https://github.com/fitnr/imagebotkit

# Licensed under the MIT license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, imagebot <fitnr@fakeisthenewreal>
import unittest
import os
from imagebotkit import imagebotkit

class testImageBotKit(unittest.TestCase):

    def setUp(self):
        self.fixtures = os.path.join(os.path.dirname(__file__), 'fixtures')

    def testValidImage(self):
        assert imagebotkit.valid_image('foo.png') is True
        assert imagebotkit.valid_image('foo.jpeg') is True
        assert imagebotkit.valid_image('foo.pdf') is False

    def generate_record(self):
        names = (os.path.join(self.fixtures, x, 'a.png')+"\n" for x in ('a', 'b'))
        with open('record.txt', 'w') as f:
            f.writelines(names)
        return names

    def testPast_posts(self):
        self.generate_record()
        past_posts = imagebotkit.past_posts('record.txt')
        assert os.path.join(self.fixtures, 'a', 'a.png') in past_posts
        os.remove('record.txt')

    def testPick_image(self):
        previous = self.generate_record()

        glob = os.path.join(self.fixtures, '[ab]/')
        picked = imagebotkit.pick_image(glob, 1, os.path.join(self.fixtures, "record.txt"))
        assert picked[0] not in previous
        os.remove('record.txt')

    def testPick_single_image(self):
        path = os.path.join(self.fixtures, 'a', 'a.png')
        picked = imagebotkit.pick_image(path)

        assert picked[0] == path

    def testUpdateRecord(self):
        paths = ['a.png', 'b.png', 'c.png']
        fn = "foo.txt"
        imagebotkit.update_record(paths, fn)

        with open(fn) as f:
            contents = f.read()

        for p in paths:
            assert p in contents

        os.remove(fn)

if __name__ == '__main__':
    unittest.main()
