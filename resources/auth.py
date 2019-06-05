from flask import request
from flask_restful import Resource
from controllers import auth
from flask_jwt_extended import create_access_token

class Auth(Resource):

    def post(self):
        if not request.is_json:
            return {"msg": "Missing JSON in request"}, 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if not username:
            return {"msg": "Missing username parameter"}, 400
        if not password:
            return {"msg": "Missing password parameter"}, 400

        if not auth.check_creds(username, password):
            return {"msg": "Bad username or password"}, 401

        access_token = create_access_token(identity=username)

        return {"access_token": access_token}
