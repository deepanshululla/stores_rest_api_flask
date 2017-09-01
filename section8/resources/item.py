from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel        

class ItemList(Resource):
    TABLE_NAME = 'items'
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
        # return {'items': list(map(lambda x:x.json(), ItemModel.query.all()))}

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
        except Exception as e:
            print(e)
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
            item_add.save_to_db()
        except:
            return {"message":"Error occured with inserting entries"}, 500
            # 500 is Internal server error
        return item_add.json(), 201
        # 201 is for object is created
    
    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if not item:
            # if item doesn't exist
            item = ItemModel(name,data['price'])
        else:
            # if item exists
            item.price = data['price']
        try:
            item.save_to_db()
        except:
            return {"message":"Error saving the entry in the database"}
        return item.json(), 201
    
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if not item:
            return {"message":"The item with name {} doesn't exist".format(name)}, 400
        # query = "DELETE FROM {table} WHERE name=%s".format(table=self.TABLE_NAME)
        try:
            item.delete_from_db()
        except:
            return {"message":"Error deleting the entry"}, 500
        return {"message":"item {} is deleted from items".format(name)}