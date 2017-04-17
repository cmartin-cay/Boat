from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CuntField(FlaskForm):
    cuntname = StringField('cuntname', validators=[DataRequired()])

class Why(FlaskForm):
    why = SelectField('why', coerce=int)

class CuntVote(FlaskForm):
    cuntvote = SubmitField("cuntvote", validators=[])