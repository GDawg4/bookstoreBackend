from rest_framework import serializers

from notes.models import Note

from books.serializers import BooksSerializer


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'content',
            'user',
            'book'
        )