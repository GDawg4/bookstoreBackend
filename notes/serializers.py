from rest_framework import serializers

from notes.models import Note

from books.serializers import BooksSerializer

class NoteSerializer(serializers.ModelSerializer):
    book = BooksSerializer(many=True)

    class Meta:
        model = Note
        fields = (
            'title',
            'notes',
            'user',
            'book'
        )