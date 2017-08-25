import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required



class DB_Handler:
    DB_NAME='data.db'
    def __init__(self):
        self.connection = sqlite3.connect(self.DB_NAME)
        self.cursor = self.connection.cursor()
    
    def execute_query(self, query, query_tuple=None):
        if query:
            if query_tuple:
                result = self.cursor.execute(query,query_tuple)
            else:
                result =self.cursor.execute(query)
            return result
        
    def __del__(self):
        self.connection.commit()
        self.connection.close()
        

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
    
    @classmethod        
    def find_by_name(cls,name):
        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        dbh=DB_Handler()
        result=dbh.execute_query(query,(name,))
        # result = cls.execute_query(query, (name,))
        if result:
            row= result.fetchone()
            if row:
                return {'item':{'name': row[0], 'price': row[1]}}
            
    @jwt_required()
    def get(self,name):
        # the name variable corresponds to {{ url }}/<variable-name> in the GET request
        try:
            item = self.find_by_name(name)
        except:
            return {'message':"Error in getting entries"}, 500
        if item:
            return item, 200
        
        return {'message':"Item not found"}, 404
    
    @classmethod
    def insert(cls,item):
        query = "INSERT INTO {table} VALUES(?,?)".format(table=cls.TABLE_NAME)
        dbh=DB_Handler()
        dbh.execute_query(query, (item["name"],item['price']))
      
    def post(self,name):
        item = self.find_by_name(name)
        if item:
            return {"message":"The item with name {name_id} already exists".format(name_id=name)}, 400
            # 400 is bad request
        data = Item.parser.parse_args()
        item_add = {"name": name, "price": data.get('price')}
        try:
            self.insert(item_add)
        except:
            return {"message":"Error occured with inserting entries"}, 500
            # 500 is Internal server error
        return item_add, 201
        # 201 is for object is created
    
    @classmethod
    def update(cls, item):
        dbh = DB_Handler()
        query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
        dbh.execute_query(query,(item['price'], item['name']))
        
    
    def put(self,name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        item_updated = {'name': name, "price": data["price"]}
        if not item:
            # if item doesn't exist
            try:
                self.insert(item_updated)
            except:
                return {"message":"Error occured with inserting entries"}, 500
        else:
            try:
                self.update(item_updated)
            except:
                return {"message":"Error occured with updating entries"}, 500
        return item_updated, 201
    
    def delete(self,name):
        item = self.find_by_name(name)
        if not item:
            return {"message":"The item with name {} doesn't exist".format(name)}, 400
        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        dbh=DB_Handler()
        try:
            dbh.execute_query(query, (name,))
        except:
            return {"message":"Error deleting the entry"}, 500
        return {"message":"item {} is deleted from items".format(name)}