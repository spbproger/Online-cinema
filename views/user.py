from flask import request
from flask_restx import Namespace, Resource
from implemented import user_service
from dao.model.user import UserSchema


user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users_all = user_service.get_all()
        return users_schema.dump(users_all), 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}

@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        return user_schema.dump(user), 200

    def put(self, uid):
        user = request.json
        user_service.update(uid, user)
        return "", 204

