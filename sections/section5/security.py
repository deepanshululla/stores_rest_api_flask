from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username,password):
    # user = username_table.get(username, None)
    user= User.find_by_username(username)
    # returns username if user exists else return None
    if user and safe_str_cmp(user.password ,password):
        return user

def identity(payload):
    "Takes in a payload which are the contents of JWT token"
    user_id = payload['identity']
    return User.find_by_id(user_id)
    
    
    
    
    