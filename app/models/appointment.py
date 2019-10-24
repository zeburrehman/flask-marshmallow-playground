from sqlalchemy.orm import relationship

from app import db
from . import Identity

class Appointment(Identity):
    def __init__(self, s_p_id, p_id):
        self.service_provider_id = s_p_id
        self.patient_id = p_id

    service_provider_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    service_provider = relationship("User", foreign_keys=[service_provider_id])
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    patient = relationship("User", foreign_keys=[patient_id])