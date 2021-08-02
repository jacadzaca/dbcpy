#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dbcpy',
    version='1.0.0',
    description="simple python library for reading WoW's DBC files",
    long_description=readme,
    author='jacadzaca',
    author_email='vitouejj@gmail.com',
    url='https://github.com/jacadzaca/dbcpy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'venv'))
)
