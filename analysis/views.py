from rest_framework import viewsets

from permissions.services import APIPermissionClassFactory
from analysis.models import Analysis
from analysis.serializers import AnalysisSerializer


class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='NotePermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': False,
                    'update': False, #TODO: is_author
                    'partial_update': False
                }
            }
        ),
    )