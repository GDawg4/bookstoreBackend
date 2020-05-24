from rest_framework import viewsets
from rest_framework.decorators import action

from notes.models import Note
from notes.serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @action(detail=True, url_path='notes-taken', methods=['post'])
    def get_notes_taken(self, request, pk=None):
        return {'state':'succes'}
