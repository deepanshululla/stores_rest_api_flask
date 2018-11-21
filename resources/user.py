from flask_restful import Resource, reqparse
try:
    from models.user import UserModel
except:
    from stores_rest_api_flask.models.user import UserModel

class Users(Resource):
    def get(self):
        # return {"users":[user.json() for user in UserModel.query.all()]}
        return {'users': list(map(lambda x:x.json(), UserModel.query.all()))}


class UserRegister(Resource):
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
        # user = UserModel(data['username'],data['password'])
        user = UserModel(**data)
        user.save_to_db()
        return {"message":"User Created"}, 201