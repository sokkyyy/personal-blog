import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://samurai:superman7577@localhost/rayblog'
    SECRET_KEY = 'personalblog'
    API_URL = "http://quotes.stormconsultancy.co.uk/random.json"

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True



config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}