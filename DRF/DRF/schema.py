import graphene
import ToDo.schema

class Query(ToDo.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

