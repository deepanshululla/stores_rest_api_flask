from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores';
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    # items = db.relationship('ItemModel')
    # this is a list of items because it is a many to one relationship
    # one store can have many items, but one item can only have one store
    # However it is an expensive operation because it will go into item table and create a 
    # reference of store for each item
    items = db.relationship('ItemModel', lazy='dynamic')
    
    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'id': self.id, 'name': self.name, 'items':[item.json() for item in self.items]}
    
    @classmethod        
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()