from flask_restful import Resource

from app.models.user import User


class UserController(Resource):
    def get(self):
        return "Testing user"