"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb://localhost:27017/flask',
    MONGO_USERNAME='bjhee',
    MONGO_PASSWORD='111111',
    MONGO_TEST_URI='mongodb://localhost:27017/test'
)

mongo = PyMongo(app)
#hihihi@@
#ggggggg
#test1
import FlaskWebProject1.views
