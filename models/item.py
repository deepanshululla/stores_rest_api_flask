try:
    from db import db
except ModuleNotFoundError:
    from stores_rest_api_flask.db import db

class ItemModel(db.Model):
    __tablename__ = 'items';
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # Here we are saying create a foreign key store_id to reference stores.id
    store = db.relationship('StoreModel')
    # we are creating store object for every item which defines the relationship to Store model
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id':self.store_id}
    
    @classmethod        
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
        # query = "SELECT * FROM {table} WHERE name=%s LIMIT 1".format(table=cls.TABLE_NAME)
        # returns an ItemModel object
    
    def save_to_db(self):
        # SQL_ALCHEMY automatically checks if the data is changed, so takes care of both insert
        # and update
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()