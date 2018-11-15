#!/usr/bin/env python3
# coding=utf-8

from datetime import datetime
from functools import wraps
from json import JSONEncoder, dumps

from alexandria.library import Book, Author, Student

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.query import Query

__date_as_string__ = False


class DataEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            fields = {}
            for field in [x for x in dir(obj)
                          if not x.startswith('_')

                          ]:
                data = obj.__getattribute__(field)
                try:
                    print('in DataEnc', data)
                    dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = "Error while encoding"
            return fields


class AlchemyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class

            fields = {}
            for field in [x for x in dir(obj)
                          if not x.startswith('_')
                          and x not in ['metadata',
                                        'query',
                                        'query_class',
                                        'generate_auth_token',
                                        'set_hash',
                                        'check_hash',
                                        'verify_auth_token',
                                        'hash',
                                        'export',
                                        'make_ident']]:
                data = obj.__getattribute__(field)
                try:
                    # print('AlchemyEncoder:', data.__class__, data)
                    dumps(data)
                    fields[field] = data
                except TypeError:

                    if isinstance(data, datetime):
                        if __date_as_string__:
                            fields[field] = str(data)
                        else:
                            fields[field] = {
                                'year': data.year,
                                'month': data.month,
                                'day': data.day,
                                'hour': data.hour,
                                'minute': data.minute,
                                'second': data.second, }

                    elif isinstance(data, InstrumentedList):
                        # fields[field] = {
                        #     x.id: x.__str__() for x in data
                        #     }
                        fields[field] = data

                    elif isinstance(data, Query):
                        # fields[field] = {
                        #     x.id: x.name for x in data.all()
                        #     }
                        fields[field] = data

                    elif isinstance(data, (Author, Book, Student,)):
                        fields[field] = data.__todict__()

                    else:
                        fields[field] = "Unhandled: ", field, data.__str__(), obj.__str__()
                        raise ValueError(
                            f"{field} is an unhandled object. can not serialise to json")

                        # obj.__serialised = True

            #print("encoded to", type(fields))
            return fields
        else:
            raise ValueError('not declarative meta')


class APIEncoder(JSONEncoder):
    def default(self, obj):

        if isinstance(obj.__class__, DeclarativeMeta):
            # print("encoding",
            #      obj.__class__,
            #      "with", AlchemyEncoder)

            return AlchemyEncoder(
                indent=None,
                check_circular=False
            ).default(obj)

