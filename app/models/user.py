from app import db
from . import Audit

class User(Audit):
    email = db.Column(db.String)
    password = db.Column(db.String)