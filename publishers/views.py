from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from publishers.models import Publisher
from publishers.serializers import PublisherSerializer
from books.models import Book
from books.serializers import BooksSerializer


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
                    'books': True,
                }
            }
        ),
    )

    @action(detail=True, methods=['get'], url_path='books')
    def books(self, request, pk=None):
        books = Book.objects.all().filter(publisher=pk)
        serialized = BooksSerializer(books, many=True)
        return Response(serialized.data)