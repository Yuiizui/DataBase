"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import jsonify
from FlaskWebProject1 import app,mongo
import pandas as pd
import numpy as np

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,      
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Group members'
    )


@app.route('/search')
@app.route('/search/<string:name>')
def about(name= None):
    """Renders the about page."""
    #cities = [tpe, nyc, ldn]

    coursemap = pd.read_excel('/Users/helen/Desktop/DataBase/FlaskWebProject1/FlaskWebProject1/coursemap.xlsx')
    #print(coursemap.shape)
    coursemap_list = {}
    nrows = coursemap.shape[0]
    for i in range(nrows):
        ser = coursemap.loc[i, :]
        
        #print(ser.index,ser.values)
        row_dict = {}

        for idx, val in zip(ser.index, ser.values):
            idx = str(idx)
            if type(val) is str:
                row_dict[idx] = val
            elif type(val) is np.int64:
                row_dict[idx] = int(val)
            elif type(val) is np.float64:
                row_dict[idx] = float(val)
            #print(row_dict)
        #coursemap_list.append(row_dict)
        coursemap_list[str(i)] = row_dict
    #print(coursemap_list)
    coursemap_user = jsonify(coursemap_list)
    #print(coursemap_list)
    # print(coursemap_user)
    #user = {'name':'Michael', 'age':18, 'scores':[{'course': 'Math', 'score': 76}]}
    
    mongo.db.users.insert(coursemap_list)
    if name is None:
        user_1 = mongo.db.users.find()
        print(user_1)
        if user_1 is not None:
            return render_template('users.html', users=[user_1])
        else:
            return 'No user found!'
         
    else:
        user = mongo.db.users.find_one({'name': name})
        if user is not None:
            return render_template('users.html', users=[user])
        else:
            return 'No user found!'
    
   
       
@app.route('/user')
@app.route('/user/<string:name>')
def user(name=None):
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )