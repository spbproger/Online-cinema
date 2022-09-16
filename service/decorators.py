import jwt
from flask import request, abort
from constants import JWT_ALGORITHM, JWT_SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        try:
            jwt.decode(data, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print(f'JWT decode error:  {e}')
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        try:
            data = jwt.decode(data, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print(f'JWT decode error:  {e}')
            abort(401)

        if data['role'] == 'admin':
            return func(*args, **kwargs)
        else:
            abort(403)

    return wrapper
