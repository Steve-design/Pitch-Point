from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField

class CommentForm(FlaskForm):
    comment = TextAreaField('Your comment...')
    submit = SubmitField('Submit')