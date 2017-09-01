from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import os
from security import authenticate, identity
from resources.user import UserRegister, Users
from resources.item import Item, ItemList

app = Flask(__name__)

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Users, '/users')

@app.before_first_request
def create_tables():
    """
        creates all tables before the first request is sent. But the database must exist beforehand
    """
    db.create_all()

if __name__=="__main__":
    host = os.getenv('IP', '0.0.0.0');
    port = int(os.getenv('PORT', 5000));
    app.config.from_object('settings')
    # do not enable this on production
    from db import db
    # why are we importing here
    # To avoid circular imports because models will also import db
    
    db.init_app(app)
    
    app.run(host=host, port=port)