# -*- coding: utf-8 -*-

# Learn more: https://github.com/pmathbliss/videosearcher/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='videosearcher',
    version='0.1.0',
    description='Video Searcher',
    long_description=readme,
    author='Paul M Bliss',
    author_email='pmathbliss@gmail.com',
    url='https://github.com/pmathbliss/videosearcher',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

