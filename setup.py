#!/usr/bin/env python

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(name='beip_collector',
      version='0.1',
      description='A simple monitoring framework for the CAPIM/BEIP project.',
      author='Christopher Bayliss',
      author_email='christopher.bayliss@unimelb.edu.au',
#      url='',
      packages=find_packages('src',exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      package_dir = {'':'src'},
      test_suite = 'nose.collector',
      tests_require = ["nose"] )

