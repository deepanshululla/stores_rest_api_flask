from db import db

class ItemModel(db.Model):
    __tablename__ = 'items';
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    price = db.Column(db.Float(precision=2))
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def json(self):
        return {'name': self.name, 'price': self.price}
    
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
        # query = "INSERT INTO {table} VALUES(%s,%s)".format(table=self.TABLE_NAME)
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()