from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user, login_required
from app.main.models import User
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import auth_blueprint as auth
from app.main import main_blueprint
from app import db



@auth.route ('/login', methods=['GET','POST'])
def login():
    login=LoginForm()
    if login.validate_on_submit():
        user=User.query.filter_by(email=login.email.data).first()
        if user is not None and user.verify_password(login.password.data):
            login_user(user, login.remember.data)
            # print(user)
            return redirect(request.args.get('next') or url_for('main_blueprint.pitches'))
        
        flash('invalid Email or password')    
    
    return render_template('auth/login.html', login=login)     

@auth.route('/signup', methods=['GET','POST'])  
def signup():
    signup=RegistrationForm()
    if signup.validate_on_submit():
        user=User(username=signup.username.data,email=signup.email.data,password=signup.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth_blueprint.login'))
    
    return render_template('auth/signup.html', signup=signup)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_blueprint.index'))