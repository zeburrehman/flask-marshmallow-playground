from uuid import uuid4
from datetime import datetime

from app import db
from . import Audit

class User(Audit):

    def __init__(self, f_name, l_name, e_mail, password, created_by):
        self.public_id = str(uuid4())
        self.first_name = f_name,
        self.last_name = l_name,
        self.email = e_mail,
        self.password = password,
        self.created_by = created_by,
        self.created_on = datetime.utcnow()

    public_id = db.Column(db.String(128), unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)