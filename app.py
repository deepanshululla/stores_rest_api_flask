from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import os
try:
    from security import authenticate, identity
    from resources.user import UserRegister, Users
    from resources.item import Item, ItemList
    from resources.store import Store, StoreList
except ModuleNotFoundError:
    from stores_rest_api_flask.security import authenticate,identity
    from stores_rest_api_flask.resources.user import UserRegister,Users
    from stores_rest_api_flask.resources.item import Item,ItemList
    from stores_rest_api_flask.resources.store import Store,StoreList



app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'secret123'
app.config['DEBUG'] = True

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Users, '/users')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')




if __name__=="__main__":
    host = os.getenv('IP', '0.0.0.0');
    port = int(os.getenv('PORT', 5000))
    if not app.config['DEBUG']:
        app.config.from_object('settings')

    # do not enable this on production
    try:
        from db import db
    except ModuleNotFoundError:
        from stores_rest_api_flask.db import db
    # why are we importing here
    # To avoid circular imports because models will also import db
    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
    db.init_app(app)
    
    app.run(host=host, port=port)