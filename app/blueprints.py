from flask import Blueprint
from flask_restful import Api

from app.controllers.test_controller import test

blueprint = Blueprint("api", __name__)

api = Api(blueprint, '/v1')

api.add_resource(test, "/test")
