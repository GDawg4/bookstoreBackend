from rest_framework import serializers

from series.models import Series

class SeriesSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        fields = (
            'title',
            'books',
            'info'
        )