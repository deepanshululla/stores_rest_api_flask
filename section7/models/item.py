from db import DB_Handler

class ItemModel:
    TABLE_NAME = 'items'
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def json(self):
        return {'name': self.name, 'price': self.price}
    
    @classmethod        
    def find_by_name(cls,name):
        query = "SELECT * FROM {table} WHERE name=%s".format(table=cls.TABLE_NAME)
        dbh=DB_Handler()
        result=dbh.execute_query_fetch_one(query,(name,))
        if result:
            row= result
            if row:
                return cls(row[0],row[1])
                # return cls(*row)
                # returns a class object with name and price as member variables.
    
    
    def insert(self):
        query = "INSERT INTO {table} VALUES(%s,%s)".format(table=self.TABLE_NAME)
        dbh=DB_Handler()
        dbh.execute_query(query, (self.name,self.price))
    
    def update(self):
        dbh = DB_Handler()
        query = "UPDATE {table} SET price=%s WHERE name=%s".format(table=self.TABLE_NAME)
        dbh.execute_query(query,(self.price,self.name))