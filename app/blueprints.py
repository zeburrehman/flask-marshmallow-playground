from flask import Blueprint
from flask_restful import Api

from app.controllers.user_controller import UserController as user_controller
from app.controllers.user_controller import UserByIdController as user_id_controller

blueprint = Blueprint("api", __name__)

api = Api(blueprint, '/v1')

api.add_resource(user_controller, "/users/", "users")
api.add_resource(user_id_controller, "/users/<string:id>", "user_details")
