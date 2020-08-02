import graphene

class Store(graphene.ObjectType):
    id         = graphene.Int()
    name       = graphene.String()
    yogiyo_url = graphene.String()

    def resolve_store(cls, info, id):
        return info.context.store_service.get_store(id)

    def resolve_stores(cls, info, limit, offset):
        return info.context.store_service.get_stores(limit, offset)
