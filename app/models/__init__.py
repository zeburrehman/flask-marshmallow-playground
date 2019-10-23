from app import db

class Identity(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)


class Audit(Identity):
    __abstract__ = True

    created_by = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    modified_by = db.Column(db.String)
    modified_on = db.Column(db.DateTime)