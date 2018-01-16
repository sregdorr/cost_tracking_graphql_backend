import graphene

import api.schema


class Query(api.schema.Query):
    pass


class Mutation(api.schema.Mutation):
    pass


# class Mutation(api.schema.Mutation, graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query, mutation=Mutation)