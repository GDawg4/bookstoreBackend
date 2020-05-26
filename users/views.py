from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from guardian.shortcuts import assign_perm

from permissions.services import APIPermissionClassFactory
from users.models import Reader
from users.serializers import ReaderSerializer
from books.models import Book
from books.serializers import BooksSerializer
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


def test(user, obj, request):
    return user.email == obj.email


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='ReaderPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': test,
                    'destroy': False,
                    'update': True,
                    'books_owned': True,
                    'all_transactions': True
                }
            }
        ),
    )

    def perform_create(self, serializer):
        print(self.request.POST.get('email'))
        user = self.request.user
        reader = serializer.save()
        assign_perm('reader.view_reader', user, reader)
        assign_perm('reader.change_reader', user, reader)
        return Response(serializer.data)

    @action(detail=False, url_path='books-owned', methods=['get'])
    def books_owned(self, request, pk=None):
        user = self.request.user
        books = Book.objects.all().filter(Q(bought_by=user)).distinct()
        serialized = BooksSerializer(books, many=True)
        return Response(serialized.data)

    @action(detail=False, methods=['get'], url_path='all-transactions')
    def all_transactions(self, request, pk=None):
        user = self.request.user
        all_transactions = Transaction.objects.all().filter(Q(buyer=user)).distinct()
        if not all_transactions:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serialized = TransactionSerializer(all_transactions, many=True)
        return Response(serialized.data)

    @action(detail=False, methods=['get'], url_path='own-transactions')
    def own_transactions(self, request, pk=None):
        user = self.request.user
        all_transactions = Transaction.objects.all().filter(Q(buyer=user), Q(given_to=user)).distinct()
        serialized = TransactionSerializer(all_transactions, many=True)
        return Response(serialized.data)

    @action(detail=False, methods=['get'], url_path='all-transactions')
    def all_transactions(self, request, pk=None):
        user = self.request.user
        all_transactions = Transaction.objects.all().filter(Q(buyer=user)).exclude(Q(given_to=user)).distinct()
        serialized = TransactionSerializer(all_transactions, many=True)
        return Response(serialized.data)