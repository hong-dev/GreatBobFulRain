import graphene

from .schema import Query
from .service import UserService
from .model import UserDao

__all__ = ['schema', 'get_services']

schema = graphene.Schema(query = Query)

class Services:
    pass

def get_services(db):
    # Instantiage DAOs
    user_dao = UserDao(db)

    services = Services()
    services.user_service = UserService(user_dao)
    
    return services
