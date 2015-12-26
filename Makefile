# This file is part of imagebot.
# https://github.com/fitnr/imagebotkit

# Licensed under the MIT license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, imagebot <fitnr@fakeisthenewreal>

.PHONY: install deploy clean
install test develop: %: README.rst
	python setup.py $*

README.rst: README.md
	pandoc $< -o $@ || touch $@
	python setup.py check --restructuredtext --strict

deploy: README.rst | clean
	python setup.py bdist_wheel
	python3 setup.py bdist_wheel
	twine upload dist/*
	git push
	git push --tags

clean: ; rm -rf dist
