from sqlalchemy.orm import relationship
from datetime import datetime

from app import db

from . import Audit

class AppointmentDetail(Audit):
    def __init__(self, app_datetime, appointment):
        self.appointment_datetime = app_datetime
        self.appointment = appointment
        self.patient_approval = False
        self.doctor_approval = False
        self.created_by = 'zrehman'
        self.created_on = datetime.utcnow()
    
    appointment_datetime = db.Column(db.DateTime, nullable=False)
    patient_approval = db.Column(db.Boolean, unique=False, default=False)
    doctor_approval = db.Column(db.Boolean,unique=False, default=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'))
    appointment = relationship('Appointment')