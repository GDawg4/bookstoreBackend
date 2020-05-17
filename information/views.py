from rest_framework import viewsets

from information.models import Information
from information.serializers import InformationSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer