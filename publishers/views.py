from rest_framework import viewsets

from publishers.models import Publisher
from publishers.serializers import PublisherSerializers

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializers