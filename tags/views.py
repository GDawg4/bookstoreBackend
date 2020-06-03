from rest_framework import viewsets

from permissions.services import APIPermissionClassFactory
from tags.models import Tag
from tags.serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='TagPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': False,
                    'update': True,
                    'partial_update': 'tag.change_tag'
                }
            }
        ),
    )