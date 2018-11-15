#!/usr/bin/env python3
# coding=utf-8
from os import system as run_cmd

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import __dbconn__, __dbfile__

__all__ = ['db_session', 'Base', 'init_db']

engine = create_engine(
    __dbconn__,
    convert_unicode=True
)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db(overwrite=False):
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()

    if overwrite:
        run_cmd("rm %s" % __dbfile__)

    from . import models as models
    if models:
        Base.metadata.create_all(bind=engine)
