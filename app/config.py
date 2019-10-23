import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'SIB_Test.db')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'SIB_Dev.db')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'SIB_Prod.db')

config_by_name = dict(
    test= TestingConfig,
    dev= DevelopmentConfig,
    prod= ProductionConfig
)