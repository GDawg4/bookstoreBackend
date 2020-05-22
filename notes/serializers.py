from rest_framework import serializers

from notes.models import Note

from books.serializers import BooksSerializer


class NoteSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'notes',
            'user',
            'book'
        )