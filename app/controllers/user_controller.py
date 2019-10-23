from flask_restful import Resource, reqparse

from app import db
from app.models.user import User
from app.schemas.user_schema import user_schema, users_schema


class UserController(Resource):
    def get(self):
        users = User.query.all()
        return   users_schema.dump(users)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('created_by', type=str)

        args = parser.parse_args()
        f_name = args["first_name"]
        l_name = args["last_name"]
        e_mail = args["email"]
        password = args["password"]
        c_by = args["created_by"]

        db.session.add(User(f_name, l_name, e_mail, password, c_by))
        db.session.commit()

        return f"{f_name} {l_name} want to create {password} with {e_mail}", 201

class UserByIdController(Resource):
    def get(self, public_id):
        user = User.query.filter(User.public_id==public_id).first()
        if user is not None:
            return user_schema.dump(user)
        return {"message": "User not found in system."}