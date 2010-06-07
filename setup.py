#!/usr/bin/python
from setuptools import setup, find_packages
import os
import glob

setup(
    name = "thundercat",
    version = "0.1",
    packages = find_packages(),

    author = "Chris Dickinson",
    author_email = "chris@neversaw.us",
    description = "python client app for nappingcat framework servers",
    long_description = """
A command line interface to nappingcat servers. Allows the user to create, fork, and delete repositories from the command line.
""".strip(),
    license = "BSD",
    keywords = "ssh git client",
    url = "http://github.com/downloads/chrisdickinson/thundercat/thundercat-0.1.tar.gz",

    entry_points = {
        'console_scripts': [
                'thundercat = thundercat.main:main',
            ],
        },

    zip_safe=False,
    install_requires=[
        'setuptools>=0.6c5',
        'importlib>=1.0.2',
        'paramiko>=1.7.4',
        ],
    )


