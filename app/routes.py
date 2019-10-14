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


@app.route('/form', methods = ['GET', 'POST'])
def form():
    form = SubmitData()
    if form.validate_on_submit() :
        flash('date{}, temp{}'.format(forms.temp.data,forms.date.data))
        return redirect('/index')
    return render_template('forms.html', form =form )
