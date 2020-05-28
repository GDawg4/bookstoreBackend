from django.db.models import Q
from django.shortcuts import get_object_or_404
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
from notes.models import Note
from notes.serializers import NoteSerializer
from analysis.models import Analysis
from analysis.serializers import AnalysisSerializer


def is_self(user, obj, request):
    return user.email == obj.email


def vibe_check(user, obj, request):
    return False


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
                    'retrieve': is_self,
                    'destroy': False,
                    'update': True,
                    'books_owned': True,
                    'all_transactions': True,
                    'buy': True
                }
            }
        ),
    )

    def perform_create(self, serializer):
        print(self.request.POST.get('email'))
        user = self.get_object()
        reader = serializer.save()
        assign_perm('reader.view_reader', user, reader)
        assign_perm('reader.change_reader', user, reader)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'], url_path='buy')
    def buy(self, request, pk=None):
        user = self.get_object()
        content = request.data.get('book')
        print(user)
        for i in content:
            book = get_object_or_404(Book, id=i)
            Transaction.objects.create(buyer=user, book=book, total=book.price, given_to=user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'], url_path='gift')
    def gift(self, request, pk=None):
        user = self.get_object()
        user_to_gift = get_object_or_404(Reader, username=user)
        content = request.data.get('books')
        for i in content:
            for key, value in i.items():
                book = Book.objects.get(id=key)
                total = book.price * int(value)
                new_transaction = Transaction.objects.create(buyer=user, book=book, total=total, given_to=user_to_gift)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, url_path='books-owned', methods=['get'])
    def books_owned(self, request, pk=None):
        user = self.get_object()
        books = Book.objects.all().filter(Q(bought_by=user)).distinct()
        serialized = BooksSerializer(books, many=True)
        return Response(serialized.data)

    @action(detail=True, methods=['get'], url_path='all-transactions')
    def all_transactions(self, request, pk=None):
        user = self.get_object()
        all_transactions = Transaction.objects.all().filter(Q(buyer=user)).distinct()
        if not all_transactions:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serialized = TransactionSerializer(all_transactions, many=True)
        return Response(serialized.data)

    @action(detail=True, methods=['get'], url_path='own-transactions')
    def own_transactions(self, request, pk=None):
        user = self.get_object()
        all_transactions = Transaction.objects.all().filter(Q(buyer=user), Q(given_to=user)).distinct()
        serialized = TransactionSerializer(all_transactions, many=True)
        return Response(serialized.data)

    @action(detail=True, methods=['get'], url_path='all-transactions')
    def all_transactions(self, request, pk=None):
        user = self.get_object()
        all_transactions = Transaction.objects.all().filter(Q(buyer=user)).exclude(Q(given_to=user)).distinct()
        serialized = TransactionSerializer(all_transactions, many=True)
        return Response(serialized.data)

    @action(detail=True, url_path='take-note', methods=['post'])
    def take_note(self, request, pk=None):
        user = self.get_object()
        title = request.data.get('title')
        content = request.data.get('content')
        book = request.data.get('book')
        Note.objects.create(title=title, content=content, book=Book.objects.get(id=book), user=user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, url_path='own_analysis', methods=['get'])
    def own_analysis(self, request, pk=None):
        user = self.get_object()
        book = request.data.get('book')
        analysis = Analysis.objects.all().filter(Q(book=book), Q(writer=user))
        serialized = AnalysisSerializer(analysis, many=True)
        return Response(serialized.data)

    @action(detail=True, url_path='see-notes', methods=['get'])
    def see_notes(self, request, pk=None):
        user = self.get_object()
        book = request.data.get('book')
        own_notes = Note.objects.all().filter(Q(user=user), Q(book=book))
        serialized = NoteSerializer
        return Response(serialized.data)

    @action(detail=True, methods=['get'], url_path='books-owned-author')
    def books_owned(self, request, pk=None):
        user = self.get_object()
        author=request.data.get('author')
        books = Book.objects.all().filter(Q(author=author), Q(bought_by=user)).distinct()
        if len(books) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serialized = BooksSerializer(books, many=True)
        return Response(serialized.data)