from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField

class PitchForm(FlaskForm):
    title = StringField('enter title')
    body = TextAreaField('lets hear your pitch')
    category = SelectField(u'Select Category', choices=[( 'Interview Pitch'), ('Product Pitch'), ( 'Pickup Lines')])
    submit=SubmitField('create pitch')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('comment')    
    submit=SubmitField('submit comment')
    