import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    API_URL = "http://quotes.stormconsultancy.co.uk/random.json"

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://samurai:superman7577@localhost/rayblog'


class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://samurai:superman7577@localhost/rayblog_test'



config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}