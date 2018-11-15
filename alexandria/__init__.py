#!/usr/bin/env python3
# coding=utf-8
from .library import init_db, db_session
from .library.models import Author, Student, Book
from .reminder import compose
from .jsonize import APIEncoder
from .endpoints import BooksListRes, BooksRes, StudentsListRes, StudentsRes, BorrowedBooks, BorrowingStudents
from json import dumps
from flask import Flask, g, make_response, send_from_directory, render_template
from flask_restful import Api
from flask_cors import CORS
import requests


app = Flask(
    __name__,
    static_folder='/static',
    template_folder='/static'
)
api = Api(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(
        dumps(
            data,
            cls=APIEncoder,
            indent=2
        ),
        code
    )
    resp.headers.extend(headers or {})
    return resp


@app.before_request
def get_db():
    if not hasattr(g, 'db'):
        g.db = db_session()


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()


all_resources = [StudentsRes, StudentsListRes, BorrowingStudents,
                 BooksRes, BooksListRes, BorrowedBooks]


for res in all_resources:
    api.add_resource(res, res.endpoint)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


# @app.route('/', defaults={'path': ''})
@app.route('/')
def index():
   # if app.debug:
   #     return requests.get(f'http://localhost:8080/{path}').text
   return render_template("index.html")
