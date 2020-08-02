class StoreService:
    def __init__(self, store_dao):
        self.store_dao = store_dao

    def get_store(self, id):
        return self.store_dao.get_store(id)

    def get_stores(self, limit, offset):
        return self.store_dao.get_stores(limit, offset)
