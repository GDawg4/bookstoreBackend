from rest_framework import serializers

from information.models import Information

class InformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = (
            'title',
            'content',
            'books_mentioned'
        )