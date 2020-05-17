from rest_framework import serializers

from reviews.models import Review

from users.serializers import UserSerializer
from books.serializers import BooksSerializer

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer(many=True)
    book = BooksSerializer(many=True)

    class Meta:
        model = Review
        fields = (
            'title',
            'score',
            'reviewer',
            'book'
        )