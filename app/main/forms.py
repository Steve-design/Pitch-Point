from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField

class CommentForm(FlaskForm):
    comment = TextAreaField('Your comment...')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.')
    submit = SubmitField('Submit')  

class PitchForm(FlaskForm):

    title = StringField('Pitch title')
    category = SelectField(u'Pitch Category', choices=[('poetry', 'poetry'), ('funny', 'funny'), ('brainy', 'brainy'),('inspiring', 'inspiring')])
    content = TextAreaField('Pitch Body')
    submit = SubmitField('Submit')      