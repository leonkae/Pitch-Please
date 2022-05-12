# from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from app import db
from app import login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,)
    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
   
    
    @property
    def password(self):
        raise AttributeError('no authorization!!!')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)
    
   
    
    
    def __repr__(self):
        return f"User {self.username}"   
        


    
    
class Pitches(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    body = db.Column(db.Text, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    votes_id = db.Column(db.Integer, db.ForeignKey('votes.id'))
    comments = db.relationship('Comments', backref='comments',lazy = True)

    
class Votes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    down_vote = db.Column(db.Integer)
    up_vote = db.Column(db.Integer)
    pitch_id = db.relationship('Pitches', backref='votes',lazy = True)
    
class Comments(db.Model):        
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text)
    # pitch_id = db.relationship('Pitches', backref='comments',lazy = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    
    
     