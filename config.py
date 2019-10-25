import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://samurai:superman7577@localhost/rayblog'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True



config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}