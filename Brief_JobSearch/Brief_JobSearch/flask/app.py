#!/usr/bin/env python
# coding: utf-8
#from app import app
#from app.models import *
from flask import Flask, request, jsonify, render_template
from flask import jsonify
from flask import request
#from flask_pymongo import PyMongo
import json
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)


client = MongoClient("localhost", 27017)
db = client["JobSearch"]
CollectionMaongodb = db["job"]
app.config["MONGO_URI"] = "mongodb://localhost:27017/JobSearch"
mongo = PyMongo(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    request.method == "POST"
    result = request.form.get('job')
    #job = result['job']
    data = CollectionMaongodb.find( {"query": result} )
    #jobs = list(data)
    #print(result)
    return render_template('index.html', job = data)

if __name__ == '__main__':
    app.run(debug=True)