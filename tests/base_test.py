"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""
import os
import sys

from unittest import TestCase


try:
    from app import app
    from db import db
    from security import authenticate, identity
except ImportError:
    from stores_rest_api_flask.app import app
    from stores_rest_api_flask.db import db


class BaseTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"

    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = BaseTest.SQLALCHEMY_DATABASE_URI
        """
        AssertionError: A setup function was called after the first request was handled.  This usually indicates a bug in the application where a module was not imported and decorators or other functionality was called too late.
        To fix this make sure to import all your view modules, database models and everything related at a central place before the application starts serving requests.

        """
        # to fix the above issue
        app.config['DEBUG'] = False
        app.config['PROPAGATE_EXCEPTIONS']=True
        with app.app_context():
            db.init_app(app)


    def setUp(self):

        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
