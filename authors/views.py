from rest_framework import viewsets

from permissions.services import APIPermissionClassFactory
from authors.models import Author
from authors.serializers import AuthorSerializer
# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='NotePermission',
            permission_configuration={
                'base': {
                    'create': False,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': False,
                    'update': False,
                    'partial_update': False
                }
            }
        ),
    )