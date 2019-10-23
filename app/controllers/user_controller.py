from flask_restful import Resource

from app.models.user import User
from app.utils import user_schema, users_schema


class UserController(Resource):
    def get(self):
        users = User.query.all()
        return   users_schema.dump(users)

    def post(self):
        return "", 200

class UserByIdController(Resource):
    def get(self, id):
        return user_schema.dump(User.query.get(id))