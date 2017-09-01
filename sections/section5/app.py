from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import os
from security import authenticate, identity
from user import UserRegister, Users
from item import Item, ItemList

app = Flask(__name__)

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Users, '/users')

if __name__=="__main__":
    host = os.getenv('IP', '0.0.0.0');
    port = int(os.getenv('PORT', 5000));
    # do not enable this on production
    app.config.from_object('settings')
    app.run(host=host, port=port)