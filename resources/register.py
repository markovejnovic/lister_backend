from flask import request
from flask_restful import Resource, reqparse, abort
from controllers import auth
from flask_jwt_extended import create_access_token

class Register(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str)
        self.parser.add_argument('password', type=str)
        super().__init__()

    def post(self):
        args = self.parser.parse_args()
        if auth.create_user(
                args['username'],
                args['password']):
            return 200
        else:
            abort(400)