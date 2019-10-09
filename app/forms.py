from flask_wtf import FlaskForm
from wtforms import DecimalField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class SubmitData(FlaskForm):
    date = DateTimeField('Date',validators = [DataRequired()], format = '%Y/%m/%d  %H:%M')
    temp = DecimalField('Temperature', validators = [DataRequired()], places = 1)
    submit = SubmitField ("Submit")
