from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q

from permissions.services import APIPermissionClassFactory
from authors.models import Author
from books.models import Book
from transactions.models import Transaction
from authors.serializers import AuthorSerializer
from books.serializers import BooksSerializer
# Create your views here.


def is_valid(user, obj, request):
    return False

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='AuthorsPermission',
            permission_configuration={
                'base': {
                    'create': False,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': False,
                    'update': False,
                    'partial_update': False,
                    'contact': is_valid,
                    'books':is_valid
                }
            }
        ),
    )

    @action(detail=True, methods=['get'], url_path='contact')
    def contact(self, request, pk=None):
        author = get_object_or_404(Author, id=pk)
        if author.has_account:
            response = author.account_linked
        elif author.contact:
            response = author.contact
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'contact': response})

    @action(detail=True, methods=['post'], url_path='books')
    def books(self, request, pk=None):
        books = Book.objects.all().filter(author=pk)
        serialized = BooksSerializer(books, many=True)
        return Response(serialized.data)

    @action(detail=True, methods=['get'], url_path='books-owned')
    def books_owned(self, request, pk=None):
        user = self.request.user
        books = Book.objects.all().filter(Q(author=pk), Q(bought_by=user)).distinct()
        if len(books) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serialized = BooksSerializer(books, many=True)
        return Response(serialized.data)