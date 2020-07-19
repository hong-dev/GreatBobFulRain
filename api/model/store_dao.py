from sqlalchemy  import text

from .base_model import BaseModel

class Store(BaseModel):
    def __init__(
        self,
        id,
        name,
        yogiyo_url
    ):
        vars = locals()
        self.__dict__.update(vars)
        del self.__dict__["self"]

class StoreDao:
    def __init__(self, db):
        self.db = db

    def get_store(self, id):
        store = self.db.execute(text("""
            SELECT
                stores.id,
                stores.name,
                stores.yogiyo_url
            FROM stores
            WHERE stores.id = :id
        """), {"id" : id}).fetchone()

        return Store.from_row(store) if store else None

    def get_stores(self, limit, offset):
        stores = self.db.execute(text("""
            SELECT
                stores.id,
                stores.name,
                stores.yogiyo_url
            FROM stores
            LIMIT  :limit
            OFFSET :offset
        """), {
            "limit"  : limit,
            "offset" : offset
        }).fetchall()

        return [ Store.from_row(store) for store in stores ]
