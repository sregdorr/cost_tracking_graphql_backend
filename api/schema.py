from graphene import relay, ObjectType, AbstractType, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene

from api.models import Client, Project


class ClientNode(DjangoObjectType):
    class Meta:
        model = Client
        filter_fields = ['client_name', ]
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        node = Client.objects.get(pk=id)
        return node


class ProjectNode(DjangoObjectType):
    class Meta:
        model = Project
        filter_fields = {
            'project_name': ['exact', 'icontains', 'istartswith'],
            'project_number': ['exact', 'icontains'],
            'client': ['exact'],
            'client__client_name': ['exact'],
        }
        interfaces = (relay.Node,)


class CreateClient(relay.ClientIDMutation):

    class Input:
        client_name = graphene.String(required=True)
        address = graphene.String()
        state = graphene.String()
        zip = graphene.String()
        contact = graphene.String()
        phone = graphene.String()
        email = graphene.String()

    client = graphene.Field(ClientNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info,
                               client_name, address=None, state=None, zip=None,
                               contact=None, phone=None, email=None, client_mutation_id=None):
        client = Client(
            client_name=client_name,
            address=address,
            state=state,
            zip=zip,
            contact=contact,
            phone=phone,
            email=email,
        )
        client.save()
        return CreateClient(client=client)


class Query(object):
    client = relay.Node.Field(ClientNode)
    all_clients = DjangoFilterConnectionField(ClientNode)

    project = relay.Node.Field(ProjectNode)
    all_projects = DjangoFilterConnectionField(ProjectNode)


class Mutation(object):
    create_client = CreateClient.Field()
