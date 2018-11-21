from flask_restful import Resource, reqparse
try:
    from models.user import UserModel
except ModuleNotFoundError:
    from stores_rest_api_flask.models.user import UserModel

class Users(Resource):
    def get(self):
        return {"users":[user.json() for user in UserModel.find_all()]}


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):
        data = UserRegister.parser.parse_args()
        print(data)
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class User(Resource):
    @classmethod
    def get(cls,user_id):
        pass
    @classmethod
    def delete(cls,user_id):
        pass
