from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id
import graphene

from api import models


# class PositionType(DjangoObjectType):
#     class Meta:
#         model = models.Position
#         filter_fields = ['position_name', 'bill_rate']
#         interfaces = (Node,)
#
#
# class EmployeeType(DjangoObjectType):
#     class Meta:
#         model = models.Employee
#         interfaces = (Node,)
#         filter_fields = ['first_name', 'last_name', 'position']
#
#
# class ClientType(DjangoObjectType):
#     class Meta:
#         model = models.Client
#         interfaces = (Node,)
#         filter_fields = ['client_name', 'address', 'contact', 'phone', 'email']
#
#
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = models.Project
#         interfaces = (Node,)
#         filter_fields = ['project_name', 'budget', 'start_date', 'end_date', 'client', 'project_lead']
#
#
# class Query(object):
#     all_positions = DjangoFilterConnectionField(PositionType)
#     position = Node.Field(PositionType)
#
#     all_employees = DjangoFilterConnectionField(EmployeeType)
#     employee = Node.Field(EmployeeType)
#
#     all_clients = DjangoFilterConnectionField(ClientType)
#     client = Node.Field(ClientType)
#
#     all_projects = DjangoFilterConnectionField(ProjectType)
#     project = Node.Field(ProjectType)
#
#     # def resolve_all_positions(self, info, **kwargs):
#     #     return models.Position.objects.all()
#
#     def resolve_all_employees(self, info, **kwargs):
#         return models.Employee.objects.all()
#
#     def resolve_all_clients(self, info, **kwargs):
#         return models.Client.objects.all()
#
#     def resolve_all_projects(self, info, **kwargs):
#         return models.Project.objects.all()
#
#
# class AddPosition(graphene.Mutation):
#     class Arguments:
#         position_name = graphene.String(required=True)
#         bill_rate = graphene.Float(required=True)
#
#     ok = graphene.Boolean()
#     position = graphene.Field(lambda: PositionType)
#
#     def mutate(self, info, **kwargs):
#         position_name = kwargs.get('position_name')
#         bill_rate = kwargs.get('bill_rate')
#
#         position = models.Position.objects.create(position_name=position_name, bill_rate=bill_rate)
#         ok = True
#         return AddPosition(ok=ok, position=position)
#
#
# class EditPosition(graphene.Mutation):
#     class Arguments:
#         id = graphene.String(required=True)
#         position_name = graphene.String()
#         bill_rate = graphene.Float()
#
#     ok = graphene.Boolean()
#     error = graphene.String()
#     position = graphene.Field(PositionType)
#
#     def mutate(self, info, **kwargs):
#         try:
#             rid = from_global_id(kwargs.get('id'))
#         except Exception:
#             return EditPosition(ok=False, error="id not found")
#
#         position = models.Position.objects.get(pk=rid[1])
#         if kwargs.get('position_name'):
#             position.position_name = kwargs.get('position_name')
#
#         if kwargs.get('bill_rate'):
#             position.bill_rate = kwargs.get('bill_rate')
#
#         position.save()
#
#         return EditPosition(ok=True, position=position)
#
#
# class AddClient(graphene.Mutation):
#     class Arguments:
#         client_name = graphene.String(required=True)
#         address = graphene.String()
#         contact = graphene.String()
#         phone = graphene.String()
#         email = graphene.String()
#
#     ok = graphene.Boolean()
#     error = graphene.String()
#     client = graphene.Field(ClientType)
#
#     def mutate(self, info, **kwargs):
#         client = models.Client.objects.create(
#             client_name=kwargs.get('client_name'),
#             address=kwargs.get('address'),
#             contact=kwargs.get('contact'),
#             phone=kwargs.get('phone'),
#             email=kwargs.get('email'),
#         )
#         return AddClient(ok=True, client=client)
#
#
# class AddEmployee(graphene.Mutation):
#     class Arguments:
#         first_name = graphene.String(required=True)
#         last_name = graphene.String(required=True)
#         position_id = graphene.String(required=True)
#
#     ok = graphene.Boolean()
#     error = graphene.String()
#     position = graphene.Field(PositionType)
#     employee = graphene.Field(EmployeeType)
#
#     def mutate(self, info, **kwargs):
#         first_name = kwargs.get('first_name')
#         last_name = kwargs.get('last_name')
#         position_id = kwargs.get('position_id')
#
#         try:
#             rid = from_global_id(position_id)
#         except:
#             return AddEmployee(ok=False, error='invalid position id')
#
#         position = models.Position.objects.get(pk=rid[1])
#         employee = models.Employee.objects.create(
#             first_name=first_name, last_name=last_name, position=position
#         )
#         ok = True
#         return AddEmployee(ok=ok, employee=employee)
#
#
# class Mutation(object):
#     add_position = AddPosition.Field()
#     edit_position = EditPosition.Field()
#     add_employee = AddEmployee.Field()
#     add_client = AddClient.Field()

