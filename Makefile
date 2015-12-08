# This file is part of imagebot.
# https://github.com/fitnr/imagebotkit

# Licensed under the MIT license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, imagebot <fitnr@fakeisthenewreal>

.PHONY: install deploy
install: README.rst
	python setup.py install

README.rst: README.md
	pandoc $< -o $@ || touch $@

deploy:
	rm -rf dist
	python setup.py bdist_wheel
	python3 setup.py bdist_wheel
	twine upload dist/*
