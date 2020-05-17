from rest_framework import serializers

from books.models import Book

from analysis.serializers import AnalysisSerializer
from information.serializers import InformationSerializer


class BooksSerializer(serializers.ModelSerializer):
    reviews_starred = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    analysis_starred = AnalysisSerializer(many=True)
    info_mentions = InformationSerializer(many=True)

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