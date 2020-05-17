from rest_framework import serializers

from publishers.models import Publisher

from books.serializers import BooksSerializer

class PublisherSerializers(serializers.ModelSerializer):
    books_published = BooksSerializer(many=True)

    class Meta:
        model = Publisher
        fields = (
            'name',
            'city',
            'books_published'
        )