# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import codecs
import os
import re
import platform
from setuptools import setup


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


required = ['colorlog', 'pyyaml']
if platform.system() == 'Windows':
    required.extend(['colorama'])

LONG_DESCRIPTION = """
**awesomelog** is a Python package providing good looking console and file
logging configuration.

awesomelog is not a new logging framework, it's only a good looking
configuration for the bult-in `logging` package.

You just import it and move on with your coding.
"""

setup(
    name='awesomelog',
    packages=['awesomelog'],
    version=find_version('awesomelog', 'awesomelog.py'),
    description='Bootstrap for console and file logging configuration',
    install_requires=required,
    long_description=LONG_DESCRIPTION,
    author='Rafael Santos',
    author_email='rstogo@outlook.com',
    url='https://github.com/rtogo/awesomelog',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
)
