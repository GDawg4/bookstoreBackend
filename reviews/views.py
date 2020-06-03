from rest_framework import viewsets

from permissions.services import APIPermissionClassFactory
from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ReviewPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': False,
                    'update': False,
                    'partial_update': False
                }
            }
        ),
    )