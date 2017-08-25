import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

items=[]

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        row = result.fetchone()
        
        connection.close()
        if row:
            return {'item':{'name': row[0], 'price': row[1]}}, 200
        
        return {'message':"Item not found"}, 404
        # return {"items": items}

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help = "This field is mandatory"
    )
    
    @jwt_required()
    def get(self,name):
        # the name variable corresponds to {{ url }}/<variable-name> in the GET request
        item = self.find_by_name(name)
        if item:
            return item
        
        return {'message':"Item not found"}, 404
      
    @classmethod
    def execute_query(cls, query, query_tuple):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute(query,query_tuple)
        connection.commit()
        connection.close()
        return result
    
    @classmethod        
    def find_by_name(cls,name):

        query = "SELECT * FROM items WHERE name=? LIMIT 1"
        result = cls.execute_query(query, (name,))
        row = result
        
        if row:
            return {'item':{'name': row[0], 'price': row[1]}}
        else:
            return
        
    
    def post(self,name):
        item = self.find_by_name(name)
        if item:
            return {"message":"The item with name {} already exists".format(name)}, 400
            # 400 is bad request
        data = Item.parser.parse_args()
        item_add = {"name": name, "price": data.get('price')}
        
        query = "INSERT INTO items VALUES(?,?)"
        self.execute_query(query, (item_add["name"],item_add['price']))
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
        return item, 201
    
    def delete(self,name):
        item = self.find_by_name(name)
        if not item:
            return {"message":"The item with name {} doesn't exist".format(name)}, 400
        query = "DELETE FROM items WHERE name=?"
        self.execute_query(query, (name,))
        
        
        return {"message":"item {} is deleted from items".format(name)}