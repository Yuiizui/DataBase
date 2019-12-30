"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

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


@app.route('/about')
@app.route('/about/<string:name>')
def about():
    """Renders the about page."""
    if name is None:
        users = mongo.db.users.find()
        return render_template('users.html', users=users)
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