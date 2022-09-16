from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def create(self, user_data):
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return user

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).one()

    def update(self, uid, user_data):
        user = self.session.query(User).get(uid)
        user.username = user_data.get('username')
        user.password = user_data.get('password')
        user.role = user_data.get('role')
        self.session.add(user)
        self.session.commit()
