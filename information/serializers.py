from rest_framework import serializers

from information.models import Information


class InformationSerializer(serializers.ModelSerializer):
    book_mentioned = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Information
        fields = (
            'title',
            'content',
            'book_mentioned'
        )