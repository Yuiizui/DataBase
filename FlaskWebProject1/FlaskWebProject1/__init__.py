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
coursemap = mongo.db.coursemap.find({})
json_zip = mongo.db.json_zip.find({})
topic = {}
lecturers = {}
course = {}
school = {}
for u1 in coursemap:
    topic[u1['name']] = []
# for u2 in json_zip:
#     lecturers[u2['cAuthor']] = []
for u2 in json_zip:
    dic = {}
    dic['Provider'] = u2['cProvider']
    dic['PhotoLink'] = u2['cPhotoLink']
    dic['DirectLink'] = u2['cDirectLink']
    dic['Description'] = u2['cDescription']
    dic['Author'] = u2['cAuthor']
    dic['label'] = u2['label']
    dic['Language'] = u2['cLanguage']
    course[u2['cTitle']] = dic
    if(lecturers.get(u2['cAuthor']) is None):
        lecturers[u2['cAuthor']] = []
    lecturers[u2['cAuthor']].append(u2['cTitle'])
    topic[u2['label']].append(u2['cTitle'])
import FlaskWebProject1.views
