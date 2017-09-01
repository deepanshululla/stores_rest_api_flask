from flask_rest import app
from flask_rest import db

app.config.from_object('settings')
db.init_app(app)

@app.before_first_request
def create_tables():
    """
        creates all tables before the first request is sent. But the database must exist beforehand
    """
    db.create_all()
