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
            created_at
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
                accounts.id,
                accounts.slack_name,
                accounts.slack_account,
                accounts.profile_image,
                accounts.slack_code,
                accounts.created_at
            FROM accounts
            WHERE (accounts.id = :id)
        """), {"id" : id}).fetchone()

        return User.from_row(user) if user else None

    def get_users(self, limit, offset):
        users = self.db.execute(text("""
            SELECT
                accounts.id,
                accounts.slack_name,
                accounts.slack_account,
                accounts.profile_image,
                accounts.slack_code,
                accounts.created_at
            FROM accounts
            ORDER BY accounts.created_at
            LIMIT  :limit
            OFFSET :offset
        """), {
            "limit"  : limit,
            "offset" : offset
        }).fetchall()

        return [User.from_row(user) for user in users]

