from rest_framework import serializers

from tags.models import Tag

from books.serializers import BooksSerializer


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = [
            'id',
            'title'
        ]