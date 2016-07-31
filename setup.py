#!/usr/bin/env python

from setuptools import setup, find_packages

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='spikefinder',
    version=version,
    description='evaluate spike finding algorithms',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    url='https://github.com/codeneuro/spikefinder-python',
    packages=find_packages(),
    install_requires=required,
    entry_points = {"console_scripts": ['spikefinder = spikefinder.cli:cli']},
    long_description='See ' + 'https://github.com/codeneuro/spikefinder-python',
    license='MIT'
)
