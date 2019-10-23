from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from app.config import config_by_name

ma = Marshmallow()
db = SQLAlchemy()

def create_app(config_env):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_env])
    ma.init_app(app)
    db.init_app(app)
    return app