# from flask_sqlalchemy import SQLAlchemy
import os
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    

    
    
class DevConfig(Config):
    DEBUG = os.environ.get('DEBUG')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://leonkae:12345678@localhost/newpitch'

class ProdConfig(Config):
    # pass
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    DEBUG = False
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://",1)
  
    


config_options = {
'development':DevConfig,
'production':ProdConfig,
}
