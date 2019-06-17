from flask_restful import Resource
from controllers import users
from flask_jwt_extended import jwt_required

class Users(Resource):

    @jwt_required
    def get(self):
        return users.get_all()

    def post(self):
        pass