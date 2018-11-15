from alexandria.library.models import Student, Book
from alexandria.library.convenience import *
from alexandria.library.db_setup import *


def recreate_db(fill=False):
    init_db(overwrite=True)
    if fill:
        import_db(Book, 'books.csv')
        import_db(Student, 'students.csv')
        #import_db(Author, 'authors.csv')


if __name__ == "__main__":
    recreate_db(fill=True)
