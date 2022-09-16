from flask import request
from flask_restx import Namespace, Resource, abort

from dao.model.user import UserSchema
from implemented import auth_service


auth_ns = Namespace('auth')
user_schema = UserSchema()


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get('username', None)
        password = req_json.get('password', None)
        if None in [username, password]:
            raise abort(404)

        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        req_json = request.json
        ref_token = req_json['refresh_token']
        print(ref_token)
        tokens = auth_service.approve_refresh_token(ref_token)
        return tokens, 201
