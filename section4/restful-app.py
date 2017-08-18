from flask import Flask
from flask_restful import Resource, Api
import os


app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self,name):
        return {"student": name}

api.add_resource(Student, '/student/<string:name>') 
# http://127.0.0.1:5000/student/deepanshu


if __name__=="__main__":
    host = os.getenv('IP', '0.0.0.0');
    port = int(os.getenv('PORT', 5000));
    app.debug = True;
    # do not enable this on production

    app.run(host=host, port=port)

        