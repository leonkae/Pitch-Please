from flask_wtf import FlaskForm
from app.main.models import User
# from main.models import User
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo,Length
# from main.models import User

class RegistrationForm(FlaskForm):
    username =StringField('User name', validators=[InputRequired(),Length(min=3, max=100)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password =PasswordField('Enter Password', validators=[InputRequired(), EqualTo('password_confirm', message="Are you sure that's your password??"), Length(min=6)])
    password_confirm = PasswordField('confirm Password', validators=[InputRequired()])
    submit=SubmitField('signup')
    
    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('user name taken!')
        
    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('Email Address in use!')  
        
class LoginForm(FlaskForm):
    email=StringField('email', validators=[InputRequired(), Email()])
    password=PasswordField('password', validators=[InputRequired()])
    remember=BooleanField('Save your login info?')
    submit=SubmitField('login')
    

    
                
          