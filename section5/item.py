from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

items=[]


class ItemList(Resource):
    def get(self):
        return {"items": items}

class Item(Resource):
    parser = reqparse.RequestParser()
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
       
    
    def post(self,item_name):
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