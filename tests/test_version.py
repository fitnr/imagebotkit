#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of imagebot.
# https://github.com/fitnr/imagebotkit

# Licensed under the MIT license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, imagebot <fitnr@fakeisthenewreal>

from imagebotkit import __version__
from unittest import TestCase

class VersionTestCase(TestCase):
    def testHasProperVersion(self):
        assert __version__ == '0.1.0'
