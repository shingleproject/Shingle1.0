#!/usr/bin/env python

from setuptools import setup

setup(name='shingle',
  version='1.1',
  description='Generation of boundary representation from arbitrary geophysical fields.',
  author='Adam Candy',
  author_email='adam.candy@imperial.ac.uk',
  license = "GNUv3",
  url='https://github.com/adamcandy/Shingle',
  packages = ['shingle'],
  install_requires = ['numpy', 'scientific', 'matplotlib']
)

