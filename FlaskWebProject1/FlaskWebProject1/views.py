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
    # coursemap = pd.read_excel('/Users/helen/Desktop/DataBase/FlaskWebProject1/FlaskWebProject1/coursemap.xlsx')
    # coursemap_list = {}
    # nrows = coursemap.shape[0]
    # for i in range(nrows):
    #     ser = coursemap.loc[i, :]
    #     row_dict = {}
    #     for idx, val in zip(ser.index, ser.values):
    #         idx = str(idx)
    #         if type(val) is str:
    #             row_dict[idx] = val
    #         elif type(val) is np.int64:
    #             row_dict[idx] = int(val)
    #         elif type(val) is np.float64:
    #             row_dict[idx] = float(val)
    #     coursemap_list[str(i)] = row_dict
    #course_ = jsonify(course)

    # u1 = [d for d in users_1]
    # u2 = [d for d in users_2]
    #print(u1)
    # for a in users_1:
    #     print(a)
    # name_cat = {}
    # for u2 in users_2:
    #     for u1 in users_1:
    #         if(u1['index']==eval(u2['tmpCateg'])[0]):
    #             print("hihi")
    #             name_cat[u1['name']] = u2['cTitle']
                
    # print(name_cat)
    # if users_1.count() is 0:
    #     for k, v in coursemap_list.items():
    #         mongo.db.users1.insert(v)
    # print(name_catego)
    # print(course)
    # tmp = course.get('Author')
    # print(tmp)
    query = '資料結構'
    column = 'label'
    tmp = mongo.db.all_course_detail.find({column:{'$regex':query}})
    if name is None:
        if tmp is not None:
            return render_template('users.html',  users=tmp,title=query)
        else:
            return 'No user found!'
         
    # else:
    #     user = mongo.db.users1.find_one({'name': name})
    #     if user is not None:
    #         return render_template('users.html', users=[users_1])
    #     else:
    #         return 'No user found!'
    
   
       
@app.route('/user')
@app.route('/user/<string:name>')
def user(name=None):
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )