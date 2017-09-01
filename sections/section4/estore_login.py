from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
import os
from security import authenticate, identity


app = Flask(__name__)
jwt = JWT(app, authenticate, identity)
# jwt implements a new endpoint behind the scenes called /auth
# with a Post method, with username and password sent in json format


api = Api(app)
items=[]
# 
#     "items": [
#         {
#             "name": "chair",
#             "price": 12.0
#         }
#     ]
# 

class ItemList(Resource):
    def get(self):
        return {"items": items}

class Item(Resource):
    # So what does parser do is it parses the request
    parser = reqparse.RequestParser()
    # we are defining the only acceptable key in the JSON body of request is price
    # If the key is not there ,it will send "This field is mandatory"
    # If additional keys are there, they will not be accessible
    parser.add_argument('price',
        type=float,
        required=True,
        help = "This field is mandatory"
    )
    @jwt_required()
    def get(self,item_name):

        filter_obj = filter(lambda x: x['name'] == item_name, items)
        item =next(filter_obj,None) 
        # for each item. If there is no item it returns None
        if item:
            return {"item": item}, 200
        else:
            return {"message":"The item doesn't exist"}, 404
        # 404 is not found
    
    def post(self,item_name):
        # data = request.get_json(silent=True)
        
        item = next(filter(lambda x: x['name'] == item_name, items),None)
        if item:
            return {"message":"The item with name {} already exists".format(item_name)}, 400
            # 400 is bad request
        data = Item.parser.parse_args()
        item_add = {"name": item_name, "price": data.get('price')}
        items.append(item_add)
        return item_add, 201
        # 201 is for object is created
    
    def put(self,item_name):
      
        data = Item.parser.parse_args()
        # 
        
        item = next(filter(lambda x: x['name'] == item_name, items),None)
        if not item:
            # if item doesn't exist
            item = {'name': item_name, "price": data["price"]}
            items.append(item)
        else:
            # item["price"]= data.get('price')
            item.update(data)
        return item
    
    def delete(self,item_name):
        global items
        # global is necessary to define we are using a global variable here
        items = list(filter(lambda x: x['name'] != item_name,items))
        # returns list of all items except the item_name mentioned
        # overwrites existing items
        return {"message":"item {} is deleted from items".format(item_name)}
    
api.add_resource(ItemList, '/items') 
api.add_resource(Item, '/item/<item_name>')



if __name__=="__main__":
    host = os.getenv('IP', '0.0.0.0');
    port = int(os.getenv('PORT', 5000));
    # do not enable this on production
    app.config.from_object('settings')
    app.run(host=host, port=port)