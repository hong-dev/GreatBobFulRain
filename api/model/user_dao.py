from sqlalchemy  import text

from .base_model import BaseModel

class User(BaseModel):
    def __init__(
        self,
        id,
        slack_name,
        slack_account,
        profile_image,
        slack_code,
        created_at,
        status
    ):
        vars = locals()
        self.__dict__.update(vars)
        del self.__dict__["self"]

class UserDao:
    def __init__(self, db):
        self.db = db

    def get_user(self, id):
        user = self.db.execute(text("""
            SELECT
                users.id,
                users.slack_name,
                users.slack_account,
                users.profile_image,
                users.slack_code,
                users.created_at,
                user_status.name as status
            FROM users
            JOIN user_status
            ON users.user_status_id = user_status.id
            WHERE users.id = :id
        """), {"id" : id}).fetchone()

        return User.from_row(user) if user else None

    def get_users(self, limit, offset):
        users = self.db.execute(text("""
            SELECT
                users.id,
                users.slack_name,
                users.slack_account,
                users.profile_image,
                users.slack_code,
                users.created_at,
                user_status.name as status
            FROM users
            JOIN user_status
            ON users.user_status_id = user_status.id
            ORDER BY users.created_at DESC
            LIMIT :limit OFFSET :offset
        """), {
            "limit"  : limit, "offset" : offset
        }).fetchall()

        return [ User.from_row(user) for user in users ]
