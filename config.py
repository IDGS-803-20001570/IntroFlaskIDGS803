import os 
from sqlalchemy import create_engine
import urllib

# Se necesitainstalar estas cosas
# pip install SQLAlchemy
# pip install Flask-SQLAlchemys
# pip install PyMySQL

class Config(object):
    SECRET_KEY='Clave_Nueva'
    SESSION_COOKIE_SECURE= False

class DevvelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URL='mysql+pymysql://usuario:contra@127.0.0.1/prueba'
    SQLALCHEMY_TRACK_MODIFICATIONS=False