from werkzeug.security import safe_str_cmp
try:
    from models.user import UserModel
except ModuleNotFoundError:
    from stores_rest_api_flask.models.user import UserModel


def authenticate(username,password):
    # user = username_table.get(username, None)
    user= UserModel.find_by_username(username)
    # returns username if user exists else return None
    if user and safe_str_cmp(user.password ,password):
        return user

def identity(payload):
    "Takes in a payload which are the contents of JWT token"
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
