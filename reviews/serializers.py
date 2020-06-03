from rest_framework import serializers

from reviews.models import Review
from users.models import Reader


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.SlugRelatedField(
        queryset=Reader.objects.all(),
        slug_field='email',
    )

    class Meta:
        model = Review
        fields = (
            'id',
            'title',
            'content',
            'score',
            'reviewer',
            'book'
        )