from __future__ import absolute_import
from setuptools import setup

setup(
    name=u'python_redis',
    version=u'0.1.7',
    description=u'Redis Client',
    long_description=u"""
Redis Client implementation for Python 3.

Copyright (c) 2018, Aditya Garg.

License: MIT (see LICENSE for details)
    """,
    packages=[u'pyredis'],
    url=u'https://github.com/adityagrg/pyredis-Python2',
    license=u'MIT',
    author=u'adityagrg',
    author_email=u'adityagrg097@gmail.com',
    test_suite=u'test',
    platforms=u'posix',
    classifiers=[
            u'License :: OSI Approved :: MIT License',
            u'Programming Language :: Python :: 3'
    ],
    setup_requires=[
        u'crc16'
    ],
    install_requires=[
        u'crc16'
    ],
    keywords=[
        u'redis'
    ]
)
