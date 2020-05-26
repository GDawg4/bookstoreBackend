from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from permissions.services import APIPermissionClassFactory
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from analysis.models import Analysis
from books.models import Book
from users.models import Reader


def vibeCheck(user, obj, request):
    return False


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='TransactionPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': False,
                    'update': True
                }
            }
        ),
    )


