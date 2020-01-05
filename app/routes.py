from flask import render_template
from app import app
from app import db
from app.models import Data
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():

    #Sample writing Data
    db.session.rollback()
    d = Data(date = datetime.now(), temp = 333.8)
    db.session.add(d)
    db.session.commit()

    temp = db.session.query(Data).all()

    return render_template('index.html',title = 'Bransgore' ,temp = temp)
