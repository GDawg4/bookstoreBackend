from rest_framework import serializers

from books.models import Book

from analysis.serializers import AnalysisSerializer
from information.serializers import InformationSerializer
from publishers.serializers import PublisherSerializer
from authors.serializers import AuthorSerializer

class BooksSerializer(serializers.ModelSerializer):
    reviews_starred = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    analysis_starred = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    info_mentions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'pub_date',
            'author',
            'publisher',
            'tags',
            'price',
            'reviews_starred',
            'analysis_starred',
            'info_mentions'
        )

