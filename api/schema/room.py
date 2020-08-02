import graphene

from .user  import User
from .store import Store

class RoomStatus(graphene.ObjectType):
    id         = graphene.Int()
    name       = graphene.String()
    created_at = graphene.types.datetime.DateTime()

    def resolve_status(cls, info):
        return {
            "id"        : cls.room_status_id,
            "name"      : cls.room_status_name,
            "created_at": cls.room_status_created_at
        }

class Room(graphene.ObjectType):
    id          = graphene.Int()
    name        = graphene.String()
    created_at  = graphene.types.datetime.DateTime()
    closed_at   = graphene.types.datetime.DateTime()
    room_status = graphene.Field(RoomStatus, resolver = RoomStatus.resolve_status)
    creator     = graphene.Field(User)
    store       = graphene.Field(Store)

    def resolve_room(cls, info, id):
        return info.context.room_service.get_room(id)

    def resolve_rooms(cls, info, limit, offset, status):
        return info.context.room_service.get_rooms(limit, offset, status)

    def resolve_creator(cls, info):
        return info.context.user_service.get_user(cls.creator_id)

    def resolve_store(cls, info):
        return info.context.store_service.get_store(cls.store_id)
