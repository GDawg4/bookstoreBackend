from rest_framework import viewsets

from series.models import Series
from series.serializers import SeriesSerializer

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer