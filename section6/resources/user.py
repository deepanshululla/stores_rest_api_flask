from flask_restful import Resource, reqparse
from models.user import UserModel
from db import DB_Handler

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
        
        if UserModel.find_by_username(data['username']):
            return {"message":"User with this username already exists"}, 400
        
        dbh= DB_Handler()
        query = "INSERT INTO {table} VALUES (NULL, %s, %s)".format(table=self.TABLE_NAME)
        try:
            dbh.execute_query(query, (data['username'],data['password']))
        except Exception as e:
            print(e)
            return {"message":"Unable to register user"}
        return {"message":"User Created"}, 201