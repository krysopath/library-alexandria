from flask import request, g
from flask_restful import Resource
from json import loads
from .library import Book, Student, Author
from sqlalchemy import and_


class BooksListRes(Resource):
    endpoint = '/api/books'

    def get(self):
        return g.db.query(Book).all()

    def post(self):
        data = loads(
            request.get_data())
        change = Book(
            title=data['title'],
            author=data['author'],
            condition=data['condition'],
        )
        g.db.add(change)
        g.db.commit()
        return {'changed': change}


class BooksRes(Resource):
    endpoint = '/api/books/<int:_id>'

    def get(self, _id):
        return {
            'books': g.db.query(Book).filter(
                Book.id == _id
            ).all()
        }

    def put(self, _id):
        change = g.db.query(Book).filter(
            Book.id == _id
        ).first()
        for p, v in loads(request.get_data()).items():
            setattr(change, p, v)
        g.db.commit()
        return {'changed': change}

    def delete(self, _id):
        item = g.db.query(Book).filter(
            Book.id == _id
        ).first()
        g.db.delete(item)
        g.db.commit()
        return {'deleted': item.id}


class StudentsListRes(Resource):
    endpoint = '/api/students'

    def get(self):
        return g.db.query(Student).all()

    def post(self):
        data = loads(request.get_data())
        try:
            change = Student(
                name=data['name'],
                surename=data['surename'],
                email=data['email'],
                personal_id=data['personal_id']
            )
            g.db.add(change)
            g.db.commit()
        except KeyError as ke:
            change = ke

        return {'changed': change}


class StudentsRes(Resource):
    endpoint = '/api/students/<int:_id>'

    def get(self, _id):
        return {
            'student': g.db.query(Student).filter(
                Student.id == _id
            ).first()
        }

    def put(self, _id):
        change = g.db.query(
            Student
        ).filter(
            Student.id == _id
        ).first()

        for p, v in loads(
            request.get_data()
        ).items():
            setattr(change, p, v)
            g.db.commit()

        return {'changed': change}

    def delete(self, _id):
        item = g.db.query(
            Student
        ).filter(
            Student.id == _id
        ).first()
        g.db.delete(item)
        g.db.commit()
        return {'deleted': item.id}


class BorrowingStudents(Resource):
    endpoint = '/api/students/borrow'

    def get(self):
        return g.db.query(Student).filter(
            Student.books != None
        ).all()


class BorrowedBooks(Resource):
    endpoint = '/api/books/borrow'

    def get(self):
        return g.db.query(Book).filter(
            Book.borrowed_by != None
        ).all()

    def post(self):
        data = loads(request.get_data())
        try:
            student_id = data['student_id']
            book_id = data['book_id']

        except KeyError as ke:
            return {"error": f"argument is missing {ke}"}

        try:
            student = g.db.query(Student).filter(
                Student.id == student_id
            ).first()
            book = g.db.query(Book).filter(
                Book.id == book_id
            ).first()

            student.books.append(book)

            g.db.commit()

        except BaseException as be:
            raise be
            #return {"problem": be}

        return {"action": f"{book} by {student}"}


class ReturnBooks(Resource):
    endpoint = '/api/books/return'

    def get(self):
        return g.db.query(Book).filter(
            Book.borrowed_by == None
        ).all()

    def post(self):
        data = loads(request.get_data())
        try:
            student_id = data['student_id']
            book_id = data['book_id']

        except KeyError as ke:
            return {"error": f"argument is missing {ke}"}

        try:
            student = g.db.query(Student).filter(
                Student.id == student_id
            ).first()
            book = g.db.query(Book).filter(
                Book.id == book_id
            ).first()
            book.borrowed_by = None
            g.db.commit()

        except BaseException as be:
            raise be
            #return {"problem": be}

        return {"action": f"{book} by {student}"}
