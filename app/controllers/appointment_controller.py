from flask_restful import Resource, reqparse
from sqlalchemy import or_
from datetime import datetime, timedelta

from app import db
from app.models.user import User
from app.models.appointment import Appointment
from app.models.appointment_detail import AppointmentDetail
from app.schemas.appointment_schema import appointment_schema, appointments_schema

class AppointmentController(Resource):
    def get(self):
        service_provider_alias = db.aliased(User)
        patient_alias = db.aliased(User)

        appointments = db.session.query(Appointment).join(service_provider_alias, (Appointment.service_provider_id==service_provider_alias.id)).join(patient_alias, (Appointment.patient_id==patient_alias.id)).all() #Appointment.query.all()
        
        return appointments_schema.dump(appointments)
    
    def post(self):
        parser = reqparse.RequestParser()
        # TODO: Change service provider id to public user id as we will be receiving public id of user. and then fetch there id from db.
        parser.add_argument('service_provider_id', type=str)
        parser.add_argument('patient_id', type=str)

        args = parser.parse_args()
        s_p_id = args["service_provider_id"]
        p_id = args["patient_id"]
        db.session.add(AppointmentDetail(datetime.utcnow() + timedelta(days=5, hours=2), Appointment(s_p_id, p_id)))
        db.session.commit()
        return "Appointment created successfully.",201
    
class UserAppointmentsController(Resource):
    def get(self, public_id):
        service_provider_alias = db.aliased(User)
        patient_alias = db.aliased(User)

        appointments = list(db.session.query(Appointment).join(service_provider_alias, Appointment.service_provider_id==service_provider_alias.id).join(patient_alias, Appointment.patient_id==patient_alias.id).filter(or_(service_provider_alias.public_id == public_id, patient_alias.public_id == public_id)))
        return appointments_schema.dump(appointments)
