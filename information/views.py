from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from information.models import Information
from information.serializers import InformationSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
