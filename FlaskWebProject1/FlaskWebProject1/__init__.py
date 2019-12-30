"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb+srv://yujui:paul1939@cluster0-omrxj.gcp.mongodb.net/test?retryWrites=true&w=majority',
    MONGO_USERNAME='yujui',
    MONGO_PASSWORD='paul1939'
)

mongo = PyMongo(app)
import FlaskWebProject1.views
