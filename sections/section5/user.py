import sqlite3
from flask_restful import Resource, reqparse

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

class Users(Resource):
    TABLE_NAME='users'
    def get(self):
        dbh = DB_Handler()
        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        try:
            result = dbh.execute_query(query)
        except:
            return {"message": "error getting users list"}, 500
        users =[]
        for row in result:
            users.append({'id':row[0],'username': row[1]})
        if users:
            return {"users":users}
        return {'message':"No users found"}, 404

class User:
    TABLE_NAME='users'
    def __init__(self, _id, username, password):
        self.id =_id
        self.username = username
        self.password = password
       
    @classmethod    
    def find_by_username(cls, username):
        dbh= DB_Handler()
        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        try:
            result = dbh.execute_query(query,(username,))
        except:
            return {"message":"Unable to exexute query to find by name"}
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        
        return user
    
    @classmethod    
    def find_by_id(cls, _id):
        dbh= DB_Handler()
        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        try:
            result = dbh.execute_query(query,(_id,))
        except:
            return {"message":"Unable to exexute query to find by id"}
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        
        return user

class UserRegister(Resource):
    TABLE_NAME='users'
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "This field is mandatory"
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = "This field is mandatory"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if User.find_by_username(data['username']):
            return {"message":"User with this username already exists"}, 400
        
        dbh= DB_Handler()
        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=self.TABLE_NAME)
        try:
            dbh.execute_query(query, (data['username'],data['password']))
        except:
            return {"message":"Unable to register user"}
        return {"message":"User Created"}, 201