class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def get_user(self, id):
        return self.user_dao.get_user(id)

    def get_users(self, limit, offset):
        return self.user_dao.get_users(limit, offset)
