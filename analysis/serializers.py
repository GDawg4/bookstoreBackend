from rest_framework import serializers

from analysis.models import Analysis


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = (
            'title',
            'content',
            'book',
            'writer'
        )