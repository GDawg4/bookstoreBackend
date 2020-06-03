from rest_framework import serializers

from publishers.models import Publisher


class PublisherSerializer(serializers.ModelSerializer):
    books_published = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Publisher
        fields = (
            'id',
            'name',
            'city',
            'country',
            'website',
            'contact',
            'publisher_pic',
            'books_published'
        )