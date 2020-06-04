from rest_framework import viewsets
from rest_framework.response import Response
from guardian.shortcuts import assign_perm

from permissions.services import APIPermissionClassFactory
from cart.models import Cart
from cart.serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='CartPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': True,
                    'update': False,
                    'partial_update': False,
                }
            }
        ),
    )

