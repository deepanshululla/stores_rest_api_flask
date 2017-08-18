#!/usr/bin/python3

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

if __name__=="__main__":
    host = os.getenv('IP', '0.0.0.0');
    port = int(os.getenv('PORT', 5000));
    app.debug = True;
    # do not enable this on production

    app.run(host=host, port=port)
