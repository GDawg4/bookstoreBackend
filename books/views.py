from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from guardian.shortcuts import assign_perm


from permissions.services import APIPermissionClassFactory
from books.models import Book
from books.serializers import BooksSerializer
from users.models import Reader
from notes.models import Note
from notes.serializers import NoteSerializer
from analysis.models import Analysis
from analysis.serializers import AnalysisSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BookPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': False,
                    'update': True,
                    'partial_update': 'pets.change_pet'
                }
            }
        ),
    )

    #Only if owns Book
    @action(detail=True, url_path='take-note', methods=['post'])
    def take_note(self, request, pk=None):
        user = self.request.user
        title = request.data.get('title')
        content = request.data.get('content')
        Note.objects.create(title=title, content=content, book=Book.objects.get(id = pk), user=user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, url_path='see-notes', methods=['get'])
    def see_notes(self, request, pk=None):
        user = self.request.user
        own_notes = Note.objects.all().filter(Q(user=user), Q(book=pk))
        serialized = NoteSerializer
        return Response(serialized.data)

    @action(detail=True, url_path='all-analysis', methods=['get'])
    def all_analysis(self, request, pk=None):
        analysis = Analysis.objects.all().filter(Q(book=pk))
        serialized = AnalysisSerializer(analysis, many=True)
        return Response(serialized.data)

    @action(detail=False, url_path='book-time', methods=['post'])
    def book_time(self, request, pk = None):
        start = request.data.get('start')
        end = request.data.get('end')
        if start and end:
            books = Book.objects.all().filter(Q(pub_date__gt=start), Q(pub_date__lt=end))
        elif start and not end:
            books = Book.objects.all().filter(Q(pub_date__gt=start))
        elif not start and end:
            books = Book.objects.all().filter(Q(pub_date__lt=end))
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serialized = BooksSerializer(books, many=True)
        return Response(serialized.data)


