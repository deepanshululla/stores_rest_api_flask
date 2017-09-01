from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from db import DB_Handler
from models.item import ItemModel        

class ItemList(Resource):
    TABLE_NAME = 'items'
    def get(self):
        dbh = DB_Handler()
        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        try:
            result = dbh.execute_query(query)
        except:
            return {"message": "error getting items list"}, 500
        items =[]
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        if items:
            return {"items":items}
        return {'message':"No items found"}, 404


class Item(Resource):
    TABLE_NAME = 'items'
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help = "This field is mandatory"
    )
    
    @jwt_required()
    def get(self,name):
        # the name variable corresponds to {{ url }}/<variable-name> in the GET request
        try:
            item = ItemModel.find_by_name(name)
            # returns an item object
        except:
            return {'message':"Error in getting entries"}, 500
        if item:
            return item.json(), 200
        
        return {'message':"Item not found"}, 404
    
    def post(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return {"message":"The item with name {name_id} already exists".format(name_id=name)}, 400
            # 400 is bad request
        data = Item.parser.parse_args()
        # item_add = {"name": name, "price": data.get('price')}
        item_add = ItemModel(name, data['price'])
        try:
            # ItemModel.insert(item_add)
            item_add.insert()
        except:
            return {"message":"Error occured with inserting entries"}, 500
            # 500 is Internal server error
        return item_add.json(), 201
        # 201 is for object is created
    
    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        # item object
        # item_updated = {'name': name, "price": data["price"]}
        item_updated = ItemModel(name,data['price'])
        if not item:
            # if item doesn't exist
            try:
                # ItemModel.insert(item_updated)
                item_updated.insert()
            except:
                return {"message":"Error occured with inserting entries"}, 500
        else:
            # if item exists
            try:
                if float(item.price) != float(data['price']):
                    item_updated.update()
            except:
                return {"message":"Error occured with updating entries"}, 500
        return item_updated.json(), 201
    
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if not item:
            return {"message":"The item with name {} doesn't exist".format(name)}, 400
        query = "DELETE FROM {table} WHERE name=%s".format(table=self.TABLE_NAME)
        dbh=DB_Handler()
        try:
            dbh.execute_query(query, (name,))
        except:
            return {"message":"Error deleting the entry"}, 500
        return {"message":"item {} is deleted from items".format(name)}