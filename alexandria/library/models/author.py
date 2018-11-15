from sqlalchemy import (
    Column, Integer,
    Sequence, String,
    UniqueConstraint,
)

from sqlalchemy.orm import relationship
from .skeleton import Skeleton
from ..db_setup import Base



__all__ = ['Author']


class Author(Skeleton, Base):
    modelname = "Author"
    __tablename__ = "authors"
    __table_args__ = (
        UniqueConstraint('surename', 'name'),
    )
    id = Column(
        Integer,
        Sequence('author_id_seq'),
        primary_key=True
    )
    surename = Column(
        String,
        #nullable=False
    )
    name = Column(
        String,
        #nullable=False
    )
    export = [
            'id',
            'name',
            'surename',
    ]
    books = relationship('Book', back_populates="author")

    def __init__(self, name=None, surename=None, *args, **kwargs):
        self.name = name
        self.surename = surename

    def __repr__(self):
        return "<Author(id=%r, surename=%r, name=%r)>" \
               % (self.id, self.surename, self.name,)

    def __str__(self):
        return "%s %s" % (self.name, self.surename)

