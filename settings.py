import os
from base64 import b64encode

random_bytes = os.urandom(64)
JWT_SECRET_KEY = b64encode(random_bytes).decode('utf-8')
SECRET_KEY = JWT_SECRET_KEY
DEBUG = True;


# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL"])
DB_URL= os.environ.get('DATABASE_URL', 'sqlite:///data.db')

# postgres://ejuairuernrnpt:ee619bf6d517efc47ec03bdbd88481a6f6ba1aaa5fffa1b74f1f0ccbc2d7595f@ec2-184-73-174-10.compute-1.amazonaws.com:5432/d2r0jn1o70llb8postgres://ejuairuernrnpt:ee619bf6d517efc47ec03bdbd88481a6f6ba1aaa5fffa1b74f1f0ccbc2d7595f@ec2-184-73-174-10.compute-1.amazonaws.com:5432/d2r0jn1o70llb8

# DB_URI = "postgresql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST,DATABASE_NAME)

SQLALCHEMY_DATABASE_URI = DB_URL;
SQLALCHEMY_TRACK_MODIFICATIONS = False;