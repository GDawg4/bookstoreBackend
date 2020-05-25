from rest_framework import viewsets
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from books.models import Book
from books.serializers import BooksSerializer
from information.models import Information
from information.serializers import InformationSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

    @action(detail=True, url_path='add', methods=['post'])
    def add_to_collection(self, request, pk=None):
        books = request.data.get('books')
        for i in books:
            book=Book.objects.get(id=i)
            Information.objects.get(id=pk).book_mentioned.add(book)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, url_path='get-books', methods=['get'])
    def get_books(self, request, pk=None):
        books = Book.objects.all().filter(info_mentions=pk)
        if not books:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serialized = BooksSerializer(books, many=True)
        return Response(serialized.data)