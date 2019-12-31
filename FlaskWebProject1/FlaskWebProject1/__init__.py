"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo
# from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017/')
# db = client['test']
# collection = db['coursemap']

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
# app.config.update(
#     MONGO_URI='mongodb+srv://yujui:paul1939@cluster0-omrxj.gcp.mongodb.net/test?retryWrites=true&w=majority',
#     MONGO_USERNAME='yujui',
#     MONGO_PASSWORD='paul1939'
# )
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False
mongo = PyMongo(app)
users_1 = mongo.db.coursemap.find({})
users_2 = mongo.db.json_zip.find({})
catego = {}
for u1 in users_1:
    catego[u1['name']] = []
for u2 in users_2:
    catego[u2['label']].append(u2['cTitle'])
import FlaskWebProject1.views
