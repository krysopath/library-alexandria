from sqlalchemy import Column, Integer, Sequence, String, TIMESTAMP, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..db_setup import Base
from .skeleton import Skeleton

__all__ = ['Student']


class Student(Base, Skeleton):
    modelname = "Student"
    __tablename__ = "students"
    __table_args__ = (
        UniqueConstraint('surename', 'name'),
    )

    id = Column(
        Integer,
        Sequence('student_id_seq'),
        primary_key=True)

    surename = Column(
        String)

    name = Column(
        String)

    email = Column(
        String,
        nullable=False,
        unique=True)

    personal_id = Column(
        String,
        nullable=False,
        unique=True)

    creation_time = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=False)

    books = relationship('Book', back_populates="borrowed_by")

    export = [
            'id',
            'name',
            'surename',
            'personal_id',
            'email',
            'creation_time',
    ]

    def __init__(self, name="", surename="", email="", personal_id="", *args, **kwargs):
        self.name = name
        self.surename = surename
        self.email = email
        self.personal_id = personal_id

    def __borrow(self, book_id):
        self.books.append()

    def __repr__(self):
        return "<Student(name=%r, surename=%r, personal_id=%r)>" \
               % (self.name, self.surename, self.personal_id)

    def __str__(self):
        return "%s %s, %s" % (self.name, self.surename, self.personal_id)
