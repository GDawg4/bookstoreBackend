from rest_framework import viewsets
from guardian.shortcuts import assign_perm

from permissions.services import APIPermissionClassFactory
from books.models import Book
from users.models import Reader
from books.serializers import BooksSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
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
