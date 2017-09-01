from db import DB_Handler


class UserModel:
    TABLE_NAME='users'
    def __init__(self, _id, username, password):
        self.id =_id
        self.username = username
        self.password = password
       
    @classmethod    
    def find_by_username(cls, username):
        dbh= DB_Handler()
        query = "SELECT * FROM {table} WHERE username=%s".format(table=cls.TABLE_NAME)
        try:
            result = dbh.execute_query_fetch_one(query,(username,))
        except:
            return {"message":"Unable to exexute query to find by name"}
        row = result
        if row:
            user = cls(*row)
        else:
            user = None
        
        return user
    
    @classmethod    
    def find_by_id(cls, _id):
        dbh= DB_Handler()
        query = "SELECT * FROM {table} WHERE id=%s".format(table=cls.TABLE_NAME)
        try:
            result = dbh.execute_query_fetch_one(query,(_id,))
        except:
            return {"message":"Unable to exexute query to find by id"}
        row = result
        if row:
            user = cls(*row)
        else:
            user = None
        
        return user