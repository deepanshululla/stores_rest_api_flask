from werkzeug.security import safe_str_cmp
from user import User


users =[
   User(1, "bob", "123")
]

username_table ={user.username : user for user in users}

userid_table = {user.id : user for user in users}

def authenticate(username,password):
    user = username_table.get(username, None)
    # returns username if user exists else return None
    if user and safe_str_cmp(user.password ,password):
        return user

def identity(payload):
    "Takes in a payload which are the contents of JWT token"
    user_id = payload['identity']
    return userid_table.get(user_id, None)
    
    
    
    
    