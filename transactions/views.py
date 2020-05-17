from rest_framework import viewsets

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer