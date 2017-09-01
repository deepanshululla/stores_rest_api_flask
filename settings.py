import os
import urlparse
from base64 import b64encode

random_bytes = os.urandom(64)
JWT_SECRET_KEY = b64encode(random_bytes).decode('utf-8')
SECRET_KEY = JWT_SECRET_KEY
DEBUG = True;


urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])
DB_URL= os.environ.get('DATABASE_URL', 'sqlite:///data.db')



# DB_URI = "postgresql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST,DATABASE_NAME)

SQLALCHEMY_DATABASE_URI = DB_URL;
SQLALCHEMY_TRACK_MODIFICATIONS = False;