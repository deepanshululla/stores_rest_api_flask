import os
import urlparse
from base64 import b64encode

random_bytes = os.urandom(64)
JWT_SECRET_KEY = b64encode(random_bytes).decode('utf-8')
SECRET_KEY = JWT_SECRET_KEY
DEBUG = True;

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

DB_USERNAME = url.username
# DB_PASSWORD = SECRET_KEY 
DB_PASSWORD=url.password
DATABASE_NAME = url.path[1:]
# DB must exists before application runs
DB_HOST = os.getenv(url.hostname, '0.0.0.0');
DB_PORT =url.port
DB_URI = "postgresql://%s:%s@%s:%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST,DB_PORT, DATABASE_NAME)


SQLALCHEMY_DATABASE_URI = DB_URI;
SQLALCHEMY_TRACK_MODIFICATIONS = True;
# SET it true if enabling migrations
# Basically SQLACHEMY has its own tracking mechanism so we are saying we don't need flask_SQL_ALCHEMy for it

