from rest_framework import serializers
#     serializers.StringRelatedField(many=True)
from users.models import User
from transactions.serializers import TransactionSerializer

class UserSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)
    reviews_written = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'name',
            'last_name',
            'transactions',
            'reviews_written'
        )