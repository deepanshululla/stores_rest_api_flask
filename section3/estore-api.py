#!/usr/bin/python3

from flask import Flask, jsonify, request, render_template, url_for
import os

app = Flask(__name__)

# Post is used to store data
# Get fetches the data

# POST /store data: {name:}
# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item
# GET /store/<string:name>/item

stores =[
        {
            'name': "my_store",
            'items': [
                    {
                        'name': "my_item",
                        'price': 15.99
                    }
                ]
        },
         {
            'name': "my_store2",
            'items': [
                    {
                        'name': "my_item",
                        'price': 18.99
                    }
                ]
        }
        
    ]

@app.route('/')
def home():
    return render_template('index-estore.html')

@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items":[]
    }
    for item in request_data["items"]:
        new_store["items"].append(item)
    stores.append(new_store)
    return jsonify(new_store)
    
    
    
@app.route('/store/<string:store_name>',methods=['GET'])
def get_store(store_name):
    # iterate over stores and see if there is a match else return an error message
    for store in stores:
        if store["name"]==store_name:
            return jsonify(store)
    # return "Sorry didn't find this store",404
    return jsonify({"message":"store not found"})

@app.route('/store',methods=['GET'])
def get_all_stores():
    # jsonify is used to convert python dictionaries to json objects
    # stores is not a dictionary but a list so we create a dictionary with only one key
    #  called 'stores'
    return jsonify({'stores': stores})

@app.route('/store/<string:store_name>/item',methods=['POST'])
def create_item_in_store(store_name):
    # iterate over stores and see if there is a match else return an error message
    request_data = request.get_json()
    for store in stores:
        if store["name"]==store_name:
            new_item={
                "name":request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(store)
    # return "Sorry didn't find this store",404
    return jsonify({"message":"store not found"})

@app.route('/store/<string:store_name>/item',methods=['GET'])
def get_items_in_store(store_name):
    # iterate over stores and see if there is a match else return an error message
    for store in stores:
        if store["name"]==store_name:
            return jsonify({"items":store["items"]})
    # return "Sorry didn't find this store",404
    return jsonify({"message":"store not found"})

# the below two functions ensure always the latest static files is served thus eliminating browser caching
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__=="__main__":
    host = os.getenv('IP', '0.0.0.0');
    port = int(os.getenv('PORT', 5000));
    app.debug = True;
    # do not enable this on production

    app.run(host=host, port=port)
