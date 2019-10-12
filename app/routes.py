from flask import render_template
from app import app
from app.forms import SubmitData

@app.route('/')
@app.route('/index')
def index():
    temp = [
    {'temp' : '20',
     'time' : '8:30'},

     {'temp' : '24',
      'time' : '9:00'}
    ]

    return render_template('index.html',title = 'Bransgore' ,temp = temp)


@app.route('/form', methods = ['GET', 'POST'])
def form():
    form = SubmitData()
    if form.validate_on_submit() :
        flash('date{}, temp{}'.format(forms.temp.data,forms.date.data))
        return redirect('/index')
    return render_template('forms.html', form =form )
