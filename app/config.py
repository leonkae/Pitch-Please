# from flask_sqlalchemy import SQLAlchemy
import os
class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # if uri and uri .startswith('postgres://'):
    #     uri = uri.replace("postgres://", "postgresql://",1)
    # SQLALCHEMY_TRACK_MODIFICATIONS = os('SQLALCHEMY_TRACK_MODIFICATIONS')
    
    
class DevConfig(Config):
    DEBUG = os.environ.get('DEBUG')

class ProdConfig(Config):
    pass


config_options = {
'development':DevConfig,
'production':ProdConfig,
}