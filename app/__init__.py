from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_wtf.csrf import CSRFProtect

# imports with Brian and Sam

from .config import config_options

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth_blueprint.login'

# from .main import models
def create_app(config_name):
    app = Flask(__name__)
    # csrf.init_app(app)
    app.config.from_object(config_options[config_name])  
    db.init_app(app)    
    login_manager.init_app(app)
   
    from .auth import auth_blueprint
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    
    return app


    
    
    