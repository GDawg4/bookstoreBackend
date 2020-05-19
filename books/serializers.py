from rest_framework import serializers

from books.models import Book

from analysis.serializers import AnalysisSerializer
from information.serializers import InformationSerializer
from publishers.serializers import PublisherSerializer
from authors.serializers import AuthorSerializer

class BooksSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    publisher = PublisherSerializer(many=False, read_only=True)
    reviews_starred = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    analysis_starred = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    info_mentions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            'title',
            'pub_date',
            'author',
            'publisher',
            'tags',
            'reviews_starred',
            'analysis_starred',
            'info_mentions'
        )

