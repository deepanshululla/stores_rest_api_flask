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
        print(query)
        dbh=DB_Handler()
        result=dbh.execute_query_fetch_one(query,(name,))
        # result = cls.execute_query(query, (name,))
        if result:
            row= result
            if row:
                return {'item':{'name': row[0], 'price': row[1]}}
    
    @classmethod
    def insert(cls,item):
        query = "INSERT INTO {table} VALUES(%s,%s)".format(table=cls.TABLE_NAME)
        print(query)
        dbh=DB_Handler()
        dbh.execute_query(query, (item["name"],item['price']))
    
    @classmethod
    def update(cls, item):
        dbh = DB_Handler()
        query = "UPDATE {table} SET price=%s WHERE name=%s".format(table=cls.TABLE_NAME)
        dbh.execute_query(query,(item['price'], item['name']))