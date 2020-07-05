import graphene

from .user import User

class Query(graphene.ObjectType):

    user = graphene.Field(
        User,
        id       = graphene.Int(default_value = 0),
        resolver = User.resolver_user
    )
    users = graphene.List(
        User,
        limit    = graphene.Int(default_value = 0),
        offset   = graphene.Int(default_value = 0),
        resolver = User.resolver_users
    )
