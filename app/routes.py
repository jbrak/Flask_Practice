from flask import render_template
from app import app
from app.forms import SubmitData
from app import db
from app.models import Data

@app.route('/')
@app.route('/index')
def index():
    temp = db.session.query(Data).all()

    return render_template('index.html',title = 'Bransgore' ,temp = temp)
