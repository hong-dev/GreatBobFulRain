import graphene

class User(graphene.ObjectType):
    id            = graphene.Int()
    slack_name    = graphene.String()
    slack_account = graphene.String()
    profiel_image = graphene.String()
    slack_code    = graphene.String()
    created_at    = graphene.types.datetime.DateTime()

    def resolver_user(cls, info, id):
        return info.context.user_service.get_user(id)
    
    def resolver_users(cls, info, limit, offset):
        return info.context.user_service.get_users(limit, offset)
