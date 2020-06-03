from rest_framework import viewsets

from permissions.services import APIPermissionClassFactory
from publishers.models import Publisher
from publishers.serializers import PublisherSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='PublisherPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': False,
                    'update': False,
                    'partial_update': False,
                }
            }
        ),
    )