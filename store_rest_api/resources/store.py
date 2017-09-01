from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        """
            gets the store info
        """
        pass
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':"Store {store_name} doesn't exists".format(store_name=name)}, 404
        
    def post(self, name):
        """
            creates the store
        """
        store = StoreModel.find_by_name(name)
        if store:
            return {'message':"Store {store_name} already exists".format(store_name=name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except Exception as e:
            print(e)
            return {'message': "Error occured while creating the store"}, 500
        return store.json(), 201
        
    def delete(self,name):
        """
            deletes the store
        """
        store = StoreModel.find_by_name(name)
        if not store:
            return {'message':"Store {store_name} doesn't exists".format(store_name=name)}, 400
        try:
            store.delete_from_db()
        except Exception as e:
            print(e)
            return {'message': "Error occured while deleting the store"}, 500
        return {'message':"Store {store_name} deleted".format(store_name=name)}
        
    
class StoreList(Resource):
    def get(self):
        """
            returns list of all stores
        """
        return {'stores':[store.json() for store in StoreModel.query.all()]}