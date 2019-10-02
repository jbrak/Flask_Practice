from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    temp = [
    {'temp' : '20',
     'time' : '8:30'},

     {'temp' : '24',
      'time' : '9:00'}
    ]

    return render_template('index.html',temp = temp)
