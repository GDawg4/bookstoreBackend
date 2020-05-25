from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from analysis.models import Analysis
from analysis.serializers import AnalysisSerializer


class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

    @action(detail=True, url_path='own_analysis', methods=['get'])
    def own_analysis(self, request, pk=None):
        user = self.request.user
        analysis = Analysis.objects.all().filter(Q(book=pk), Q(writer=user))
        serialized = AnalysisSerializer(analysis, many=True)
        return Response(serialized.data)