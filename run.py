from app import app
from db import db
from flask.ext.heroku import Heroku

db.init_app(app)

@app.before_first_request
def create_tables():
    """
        creates all tables before the first request is sent. But the database must exist beforehand
    """
    db.create_all()
