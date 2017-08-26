import os
from base64 import b64encode

random_bytes = os.urandom(64)
JWT_SECRET_KEY = b64encode(random_bytes).decode('utf-8')
SECRET_KEY = JWT_SECRET_KEY
DEBUG = True;

DB_USERNAME = 'deepanshululla'
DB_PASSWORD = '' #not required for c9
DATABASE_NAME = 'flask_rest_db'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI;
SQLALCHEMY_TRACK_MODIFICATIONS = True;
