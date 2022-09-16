from dao.genre import GenreDAO
from service.decorators import auth_required,admin_required


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    @auth_required
    def get_one(self, bid):
        return self.dao.get_one(bid)

    @auth_required
    def get_all(self):
        return self.dao.get_all()

    @admin_required
    def create(self, genre_d):
        return self.dao.create(genre_d)

    @admin_required
    def update(self, genre_d):
        self.dao.update(genre_d)
        return self.dao

    @admin_required
    def delete(self, rid):
        self.dao.delete(rid)
