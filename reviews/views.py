from rest_framework import viewsets
from rest_framework.response import Response
from guardian.shortcuts import assign_perm

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
                    'destroy': 'reviews.delete_review',
                    'update': False,
                    'partial_update': False
                }
            }
        ),
    )

    def perform_create(self, serializer):
        review = serializer.save()
        user = self.request.user
        assign_perm('carts.delete_cart', user, review)
        return Response(serializer.data)