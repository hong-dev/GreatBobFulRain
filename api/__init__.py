import graphene

from .schema  import Query
from .service import (
    UserService,
    RoomService,
    StoreService
)
from .model   import (
    UserDao,
    RoomDao,
    StoreDao
)

__all__ = ['schema', 'get_services']

schema = graphene.Schema(query = Query)

class Services:
    pass

def get_services(db):
    # Instantiage DAOs
    user_dao  = UserDao(db)
    room_dao  = RoomDao(db)
    store_dao = StoreDao(db)

    services = Services()
    services.user_service  = UserService(user_dao)
    services.room_service  = RoomService(room_dao)
    services.store_service = StoreService(store_dao)

    return services
