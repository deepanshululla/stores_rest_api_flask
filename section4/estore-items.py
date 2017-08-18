from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os


app = Flask(__name__)
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
    def get(self,item_name):
        # for item in items:
        #     if item["name"]==item_name:
        #         return item
        
        filter_obj = filter(lambda x: x['name'] == item_name, items)
        # this returns a filter obj
        # item_list =list(filter_obj) # gives list of items
        # item_tuple =tuple(filter_obj) # gives tuple of items
        item =next(filter_obj,None) # gives the first match in items, is good because we know we have unique names
        # for each item. If there is no item it returns None
        if item:
            return {"item": item}, 200
        else:
            return {"message":"The item doesn't exist"}, 404
        # 404 is not found
    
    def post(self,item_name):
        # data = request.get_json(force=True)
        # It is not necessary that sometimes the request might contain the content-type header
        # to be set to json or the ody may not contain json
        # force=true sets that whatever the body is convert it to json
        
        data = request.get_json(silent=True)
        # silent=True returns null if the header is not set or body is not json
        #  request.get_json will return a python dictionary
        
        
        # checking if item with similar name exists
        # for item in items:
        #     if item["name"]==item_name:
        #         return {"message":"The item already exists"}
        item = next(filter(lambda x: x['name'] == item_name, items),None)
        if item:
            return {"message":"The item with name {} already exists".format(item_name)}, 400
            # 400 is bad request
                
        item_add = {"name": item_name, "price": data.get('price')}
        items.append(item_add)
        return item_add, 201
        # 201 is for object is created
    
    def put(self,item_name):
        pass
    
api.add_resource(ItemList, '/items') 
api.add_resource(Item, '/item/<string:item_name>')



if __name__=="__main__":
    host = os.getenv('IP', '0.0.0.0');
    port = int(os.getenv('PORT', 5000));
    app.debug = True;
    # do not enable this on production

    app.run(host=host, port=port)

        