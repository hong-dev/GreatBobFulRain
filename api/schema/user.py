import graphene

class UserStatus(graphene.ObjectType):
    user_status = graphene.String()

    def resolve_status(cls, info):
        return {"user_status" : cls.status}

class User(graphene.ObjectType):
    id            = graphene.Int()
    slack_name    = graphene.String()
    slack_account = graphene.String()
    profile_image = graphene.String()
    slack_code    = graphene.String()
    created_at    = graphene.types.datetime.DateTime()
    status        = graphene.Field(UserStatus, resolver = UserStatus.resolve_status)

    def resolve_user(cls, info, id):
        return info.context.user_service.get_user(id)
    
    def resolve_users(cls, info, limit, offset):
        return info.context.user_service.get_users(limit, offset)
