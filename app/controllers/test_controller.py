from flask_restful import Resource

class test(Resource):
    def get(self):
        return "Hello World"