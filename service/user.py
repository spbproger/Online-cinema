import base64
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from hashlib import pbkdf2_hmac
from dao.user import UserDAO


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.dao = user_dao

    def create(self, user_data):
        user_data['password'] = self.get_hash(user_data['password'])
        return self.dao.create(user_data)

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()


    # Для AuthService
    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def update(self, uid, user_data):
        if user_data.get('password'):
            user_data['password'] = self.get_hash(user_data['password'])
        return self.dao.update(uid, user_data)

    def get_hash(self, password):
        return base64.b64encode(pbkdf2_hmac('sha256',
                                password.encode('utf-8'),
                                PWD_HASH_SALT,
                                PWD_HASH_ITERATIONS))

    def compare_passwords(self, password_hashed, password):
        digest_decoded = base64.b64decode(password_hashed)
        digest_hashed = pbkdf2_hmac('sha256',
                                password.encode('utf-8'),
                                PWD_HASH_SALT,
                                PWD_HASH_ITERATIONS)

        return hmac.compare_digest(digest_decoded, digest_hashed)
