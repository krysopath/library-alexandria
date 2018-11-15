#!/usr/bin/env python3
# coding=utf-8
from os import environ
import os

path = os.path.dirname(__file__)
__home__ = '{}//%s'.format(environ['HOME'])
#__pwd__ = '{}//%s'.format(environ['PWD'])
__dbfile__ = f'{path}/library.db'
__sqlite__ = 'sqlite:///{}'.format(__dbfile__)
__dbconn__ = os.getenv("DATABASE_URL", __sqlite__)
__countrycode__ = "DE"
print(__dbconn__)