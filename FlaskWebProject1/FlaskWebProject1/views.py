"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from flask import jsonify
from FlaskWebProject1 import app,mongo
import pandas as pd
import numpy as np
from py2neo import Graph


@app.route('/')
@app.route('/',methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    # if request.method == 'POST':
    #     name = request.values['name']
    #     email = request.values['email']
    #     message = request.values['message']
    #     mongo.db.discussion_board.insert({ 'name': name, 'email': email,'message':message })
    return render_template(
        'index_2.html',
        title='Home Page',
        year=datetime.now().year,      
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        message='Group members'
    )


@app.route('/search',methods=['GET', 'POST'])
@app.route('/search/<string:name>',methods=['GET', 'POST'])
def about(name= None):
    """Renders the about page."""
    # mongo.db.create_collection('grade')
    #mongo.db.student_detail.remove()
    # student_detail = pd.read_excel('/Users/helen/Desktop/grade.xlsx')
    # student_detail_list = {}
    # nrows = student_detail.shape[0]
    # #print(nrows)
    # for i in range(nrows):
    #     ser = student_detail.loc[i, :]
    #     row_dict = {}
    #     for idx, val in zip(ser.index, ser.values):
    #         idx = str(idx)
    #         if type(val) is str:
    #             row_dict[idx] = val
    #         elif type(val) is np.int64:
    #             row_dict[idx] = int(val)
    #         elif type(val) is np.float64:
    #             row_dict[idx] = float(val)
    #     student_detail_list[str(i)] = row_dict
    # coursemap_user = jsonify(student_detail_list)
    # users1 = mongo.db.users1.find()
    # users2 = mongo.db.users2.find()
    #users3 = mongo.db.all_course_detail.find()
    # student_detail = mongo.db.grade.find()
    # print(student_detail.count())
    # if student_detail.count() is 0:
    #     for k, v in student_detail_list.items():
    #         mongo.db.grade.insert(v)
    users3 = ''
    if name is None:
        if users3 is not None:
            print(request.method)
            if request.method == 'POST':
                query = request.values['input_text']
                column = request.values['input_cat']
                print(query,column)
                tmp = mongo.db.all_course_detail.find({column:{'$regex':query}})
                print(tmp)
                return render_template('search.html',  users=tmp)
            else:
                return render_template('search.html',  users='')
        else:
            return render_template('search.html',  users='')
    # else:
    #     user = mongo.db.users.find_one({'name': name})
    #     if user is not None:
    #         return render_template('users.html', users=[user])
    #     else:
    #         return 'No user found!'

@app.route('/student',methods=['GET', 'POST'])
@app.route('/student/<string:name>',methods=['GET', 'POST'])
def student(name= None):
    """Renders the about page."""
    student_detail_grade = mongo.db.student_detail_course.find({'used_id':23})
    for a in student_detail_grade:
        print(a)
    if name is None:
        if student_detail_grade is not None:
            print(request.method)
            if request.method == 'POST':
                query = str(request.values['input_text'])
                column = str(request.values['input_cat'])
                if(column=='user_name'):
                    query = query.replace(" ","\xa0")
                print(query)
                print(column)
                if(column=='used_id' or column=='enrollment_date'):
                    find_detail = mongo.db.student_detail_course.find({column:int(query)})
                else:
                    find_detail = mongo.db.student_detail_course.find({column:{'$regex':query}})
                #student_detail_grade = mongo.db.student_detail_course.find({'used_id':10})
                # print(tmp)
                # for a in student_detail_grade:
                #     print(a)
                return render_template('student.html',  users=find_detail)
            else:
                return render_template('student.html',  users="")
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


@app.route('/graph',methods=['GET', 'POST'])
@app.route('/graph/<string:name>',methods=['GET', 'POST'])
def graph(name= None):
    
    #https://hobby-fljoljlkjmgggbkedobbdgel.dbs.graphenedb.com:24780/db/data/
    #bolt://hobby-fljoljlkjmgggbkedobbdgel.dbs.graphenedb.com:24787
    graph = Graph("bolt://hobby-fljoljlkjmgggbkedobbdgel.dbs.graphenedb.com:24787", username="adm", password="b.PZvb6ZSYxW2J.MTZodvtz6QoxLrWR",secure=True)
    if request.method == 'GET':
        nodes=graph.run('MATCH (s:Area) RETURN s.id AS id,s.name AS name').data()
        return render_template(
            'graph.html',
            title='Graph',
            nodes=nodes
        )
        #g=graph.run('MATCH (s:Area)-[:advance]->(t:Area) WHERE s.id=6 RETURN t.id').data()
        pass
    if request.method == 'POST':
        node = str(request.values['node'])
        relation = str(request.values['relation'])
        nodes=graph.run('MATCH (s:Area)-[:'+relation+']->(t:Area) WHERE s.id='+str(node)+' RETURN t.id AS id, t.name AS name').data()
        return render_template(
            'graph.html',
            title='Graph',
            nodes=nodes
        )
@app.route('/discussion',methods=['GET', 'POST'])
@app.route('/discussion/<string:name>',methods=['GET', 'POST'])
def discussion(name= None):
    """Renders the about page."""
    discussion_board = mongo.db.discussion_board.find({})
    if name is None:
        if discussion_board is not None:
            if request.method == 'POST':
                name = request.values['name']
                email = request.values['email']
                message = request.values['message']
                mongo.db.discussion_board.insert({ 'name': name, 'email': email,'message':message })
            return render_template('discussion.html',  users=discussion_board)
        else:
            return 'No user found!'