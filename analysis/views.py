from rest_framework import viewsets

from analysis.models import Analysis
from analysis.serializers import AnalysisSerializer

class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer