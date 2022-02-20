#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='dbcpy',
    version='1.0.3',
    description="simple python library for reading WoW's DBC files",
    long_description=readme,
    long_description_content_type='text/markdown',
    author='jacadzaca',
    author_email='vitouejj@gmail.com',
    url='https://github.com/jacadzaca/dbcpy',
    license='LGPL3',
    packages=find_packages(exclude=('tests', 'docs', 'venv'))
)
