import csv

from .db_setup import db_session
from .models import Book, Student, Author


def load_from_csv(filepath):
    with open(filepath, 'r') as infile:
        reader = csv.DictReader(infile)
        return [row for row in reader]


def import_db(DataModel, datafile):
    data = load_from_csv(datafile)
    for item in data:
        db_session.flush()
        if DataModel == Book:
            author = Author.query.filter(
                Author.name == item['name']
                and Author.surename == item['surename']
            ).first()
            if author:
                item['author'] = author
            else:
                item['author'] = Author(
                    item['name'],
                    item['surename']
                )

        db_session.add(
            DataModel(**item)
        )
        print(
            DataModel.__name__,
            'added with', item
        )
    db_session.commit()


def export_db(DataModel, dumpfile):
    with open(dumpfile, 'w') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=DataModel.export
        )
        writer.writeheader()

        for item in DataModel.query.all():
            writer.writerow(
                dict(item)
            )


def add_dataset(dataset, Model):
    db_session.add(
        Model(**dataset)
    )
    db_session.flush()


def add_book(bookdata):
    add_dataset(bookdata, Book)


def add_student(studentdata):
    add_dataset(studentdata, Student)


def add_author(authordata):
    add_dataset(authordata, Author)

