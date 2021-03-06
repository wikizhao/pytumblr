#!/usr/bin/env python

from setuptools import setup

setup(

    name="PyTumblr",
    version="0.0.5",
    description="A Python API v2 wrapper for Tumblr",
    author="John Bunting",
    author_email="johnb@tumblr.com",
    url="https://github.com/tumblr/pytumblr",
    packages = ['pytumblr'],
    license = "LICENSE",

    test_suite='nose.collector',

    install_requires = [
        'oauth2',
        'httpretty'
    ],

    setup_requires=[
        'nose',
        'nose-cov'
    ]

)
