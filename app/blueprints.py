from flask import Blueprint
from flask_restful import Api

from app.controllers.user_controller import UserController as user_controller
from app.controllers.user_controller import UserByIdController as user_id_controller
from app.controllers.appointment_controller import AppointmentController as appointment_controller
from app.controllers.appointment_controller import UserAppointmentsController as user_appointment_controller

blueprint = Blueprint("api", __name__)

api = Api(blueprint, '/v1')

api.add_resource(user_controller, "/users/", "users")
api.add_resource(user_id_controller, "/users/<string:public_id>", "user_details")
api.add_resource(appointment_controller, "/appointments/", "appointments")

api.add_resource(user_appointment_controller, "/appointments/<string:public_id>", "user_appointments")