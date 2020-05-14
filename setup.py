#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pymonetize",
    version="1.0",
    description="Easily add Monetization python web projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wangonya/pymonetize",
    author="Kinyanjui Wangonya",
    author_email="kwangonya@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'halo'
    ],
    entry_points='''
        [console_scripts]
        pymonetize=cli:main
    ''',
)
