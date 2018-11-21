
class Config(object):
    import os
    from base64 import b64encode

    random_bytes = os.urandom(64)
    JWT_SECRET_KEY = 'secret123'
    SECRET_KEY = JWT_SECRET_KEY
    DEBUG = True
    # PROPAGATE_EXCEPTIONS=True



    DB_USERNAME = 'deepanshululla'
    # DB_PASSWORD = SECRET_KEY
    DB_PASSWORD = ''  # not required for c9
    DATABASE_NAME = 'flask_rest_db'
    # DB must exists before application runs
    DB_HOST = os.getenv('IP', '0.0.0.0')

    # DB_URI = "postgresql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST,DATABASE_NAME)
    DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = DB_URI


    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SET it true if enabling migrations
    # Basically SQLACHEMY has its own tracking mechanism so we are saying we don't need flask_SQL_ALCHEMy for it

