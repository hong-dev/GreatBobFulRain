import graphene

from .user  import User
from .room  import Room, CreateRoom
from .store import Store

class Query(graphene.ObjectType):

    user = graphene.Field(
        User,
        id       = graphene.Int(default_value = 0),
        resolver = User.resolve_user
    )

    users = graphene.List(
        User,
        limit    = graphene.Int(default_value = 0),
        offset   = graphene.Int(default_value = 0),
        resolver = User.resolve_users
    )

    room = graphene.Field(
        Room,
        id       = graphene.Int(default_value = 0),
        resolver = Room.resolve_room
    )

    rooms = graphene.List(
        Room,
        limit    = graphene.Int(default_value = 0),
        offset   = graphene.Int(default_value = 0),
        status   = graphene.Int(default_value = 1),
        resolver = Room.resolve_rooms
    )

    store = graphene.Field(
        Store,
        id       = graphene.Int(default_value = 0),
        resolver = Store.resolve_store
    )

    stores = graphene.List(
        Store,
        limit    = graphene.Int(default_value = 0),
        offset   = graphene.Int(default_value = 0),
        resolver = Store.resolve_stores
    )

class Mutations(graphene.ObjectType):
    create_room = CreateRoom.Field()
