# from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from app import db
from app import login_manager
from flask_login import UserMixin

# db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,)
    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    
    @property
    def password(self):
        raise AttributeError('no authorization!!!')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)
    
    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))
    
    
    def __repr__(self):
        return f"User {self.username}"   
        

# class Categories(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)
#     pitch_id = db.relationship('Pitches', backref='category',lazy = True)
    
    
class Pitches(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user = db.relationship(User, backref=db.backref('pitches', lazy=True))
    # category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # category = db.relationship(Categories, backref=db.backref('pitches',lazy = True))
    votes_id = db.Column(db.Integer, db.ForeignKey('votes.id'))
    # votes = db.relationship('Votes', backref=db.backref('votes',lazy = True))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    # comments = db.relationship('Comments', backref=db.backref('comments',lazy = True))
    
class Votes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    down_vote = db.Column(db.Integer)
    up_vote = db.Column(db.Integer)
    pitch_id = db.relationship('Pitches', backref='votes',lazy = True)
    
class Comments(db.Model):        
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text)
    pitch_id = db.relationship('Pitches', backref='comments',lazy = True)
    
    
     