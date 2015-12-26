#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of imagebot.
# https://github.com/fitnr/imagebotkit

# Licensed under the GPL-3.0 license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, imagebot <fitnr@fakeisthenewreal>

from setuptools import setup, find_packages

try:
    readme = open('./README.rst', 'r').read()
except IOError:
    readme = ''

setup(
    name='imagebot',
    version='0.1.0',
    description='Kit for a simple bot that uploads images to twitter',
    long_description=readme,
    keywords='twitter bot image',
    author='imagebot',
    author_email='fitnr@fakeisthenewreal',
    url='https://github.com/fitnr/imagebotkit',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    test_suite='tests',
    install_requires=[
        'twitter_bot_utils>=0.9.7.1,<1'
    ],
    entry_points={
        'console_scripts': [
            'imagebot=imagebotkit.cli:main',
        ],
    },
)
