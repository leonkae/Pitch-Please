import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

# imports with Brian and Sam
from flask_script import Manager, Server

from flask_login import LoginManager
from .config import config_options


login_manager=LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login' '''to do list'''
db = SQLAlchemy()
csrf = CSRFProtect()

# from .main import models
migrate = Migrate()
def create_app():
    app = Flask(__name__)
    csrf.init_app(app)
    
    app.config.from_object(config_options['development'])
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://leonkae:12345678@localhost/pitchme'
    app.config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'WREWH9WEHGIOEHWGIOEHGNES'
  
    db.init_app(app)

    migrate.init_app(app,db)
   
    
   
    login_manager.init_app(app)
    from .auth import auth_blueprint
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    
    return app



if __name__ == '__main__':
    load_dotenv(find_dotenv())

    create_app()
    app.run()
   
    
    
    