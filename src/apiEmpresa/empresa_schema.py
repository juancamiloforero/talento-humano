from graphene_django import DjangoObjectType
from convocatorias.models import User as UserModel, Convocatoria as ConvocatoriaModel
from graphene import ObjectType, relay, String, ID, Int
from graphene_django.filter import DjangoFilterConnectionField
import graphql_jwt
import graphene
from graphql_jwt.decorators import login_required


class Convocatoria(DjangoObjectType):
    """Nodo del grafo"""
    class Meta:
        model = ConvocatoriaModel
        filter_fields = ['state']
        # interfaces = (relay.Node,)
    
    # @classmethod
    # def get_node(cls, info, id):
    #     if info.context.user.is_authenticated:
    #         return get_convocatoria(id)
    #     return get_convocatoria(0)


class Query(ObjectType):
    """Consultas de la app empresa"""
    convocatoria = graphene.Field(Convocatoria, id=Int())
    # convocatoria = graphene.Field(Convocatoria, id=Int())
    # convocatoria = relay.Node.get_node_from_global_id(info, id)
    # convocatorias = DjangoFilterConnectionField(Convocatoria)

    def resolve_convocatoria(self, info, *args, **kwargs):
        id = kwargs.get('id')
        if not info.context.user.is_authenticated:
            # Verificar inicio con empresa
            raise Exception('Authentication credentials were not provided!')
        #elif not info.context.user.is_company:
        #    raise Exception('Permisos insuficientes!')
        return ConvocatoriaModel.objects.get(pk=id)


from graphene_django.forms.mutation import DjangoModelFormMutation
from convocatorias.forms import ConvocatoriaModelForm
class ConvocatoriaMutation(DjangoModelFormMutation):
    class Meta:
        form_class = ConvocatoriaModelForm
        fields = ['position', 'description', 'closing_time', 'state', 'company']

class Mutation(ObjectType):
    # Creación de convocatoria
    convocatoria = ConvocatoriaMutation.Field()

    # Tokens por JWT
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

