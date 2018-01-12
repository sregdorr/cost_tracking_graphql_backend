from django.shortcuts import render
from graphene_django.views import GraphQLView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from django.views.decorators.csrf import csrf_exempt

from api import models
from api import serializers
from api.mixins.view_mixins import MultiSerializerViewSetMixin

from api.authentication import CsrfExemptSessionAuthentication


class CsrfExemptGraphQLView(GraphQLView):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(CsrfExemptGraphQLView, cls).as_view(*args, **kwargs)
        return csrf_exempt(view)


class PrivateGraphQLView(GraphQLView):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(PrivateGraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        view = authentication_classes((TokenAuthentication,))(view)
        view = api_view(['POST'])(view)
        return view

