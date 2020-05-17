from rest_framework import serializers

from transactions.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = (
            'transaction_id',
            'total',
            'buyer',
            'books'
        )