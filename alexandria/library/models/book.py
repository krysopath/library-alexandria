from sqlalchemy import Column, Integer, Sequence, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from uuid import uuid4

from ..db_setup import Base
from .author import Author
from .skeleton import Skeleton

__all__ = ['Book']


class Book(Base, Skeleton):
    modelname = "Book"
    __tablename__ = "books"
    id = Column(
        Integer,
        Sequence('book_id_seq'),
        primary_key=True
    )
    title = Column(
        String,
        #nullable=False
    )
    condition = Column(
        String,
        #nullable=False
    )
    identity = Column(
        String,
        unique=True,
        #nullable=False
    )

    author = relationship(
        "Author", back_populates="books")

    author_id = Column(
        Integer,
        ForeignKey('authors.id')
    )

    borrowed_by = relationship(
        "Student", back_populates="books")

    student_id = Column(
        Integer,
        ForeignKey('students.id')
    )

    # parent_id = Column(Integer, ForeignKey('parent.id'))
    # parent = relationship("Author", back_populates="")

    export = [
        'identity',
        'title',
        'author',
        'condition',
        'borrowed_by',
    ]

    def __init__(self, title=None, author=None, condition=None, *args, **kwargs):
        self.title = title
        self.author = author
        self.condition = condition
        self.make_ident()

    def __repr__(self):
        return "<Book(title=%r, identity=%r)>" \
               % (self.title, self.identity,)

    def __str__(self):
        return "%s by %s" % (self.title, self.author)

    def make_ident(self):
        self.identity = str(
            uuid4()
        )
#
# Author.books = relationship(
#     "Book",
#     order_by=Book.id,
#     back_populates="author")
