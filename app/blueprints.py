from flask import Blueprint
from flask_restful import Api

from app.controllers.user_controller import UserController as user_controller

blueprint = Blueprint("api", __name__)

api = Api(blueprint, '/v1')

api.add_resource(user_controller, "/user")
