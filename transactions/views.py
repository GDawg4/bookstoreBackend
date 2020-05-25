from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from permissions.services import APIPermissionClassFactory
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from books.models import Book
from users.models import Reader


def vibeCheck(user, obj, request):
    return False


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['POST'], url_path='buy')
    def buy(self, request, pk=None):
        user = self.request.user
        content = request.data.get('book')
        for i in content:
            for key, value in i.items():
                book = get_object_or_404(id=key)
                total = book.price*int(value)
                Transaction.objects.create(buyer=user, book=book, total=total)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='gift')
    def gift(self, request, pk=None):
        user = request.data.get('username')
        user_to_gift = get_object_or_404(Reader, username=user)
        content = request.data.get('books')
        for i in content:
            for key, value in i.items():
                book = Book.objects.get(id=key)
                total = book.price*int(value)
                new_transaction = Transaction.objects.create(buyer=user_to_gift, book=book, total=total)
        return Response(status=status.HTTP_200_OK)