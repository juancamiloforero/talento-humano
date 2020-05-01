from graphene import ObjectType, String, Schema
from .empresa_schema import Query as EmpresaQuery, Mutation as EmpresaMutation

class Query(EmpresaQuery):
    pass

class Mutation(EmpresaMutation):
    pass

ROOT_SCHEMA = Schema(query=Query, mutation=Mutation)