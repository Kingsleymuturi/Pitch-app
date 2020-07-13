import os
from dotenv import load_dotenv
load_dotenv()
from instance.config import DATABASE_URL, MAIL_USERNAME, MAIL_PASSWORD, SECRET_KEY

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY= SECRET_KEY 
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = MAIL_USERNAME
    MAIL_PASSWORD = MAIL_PASSWORD

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}