from rest_framework import serializers
#     serializers.StringRelatedField(many=True)
from users.models import User
from transactions.serializers import TransactionSerializer
from reviews.serializers import ReviewSerializer

class UserSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)
    reviews_written = ReviewSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'name',
            'last_name',
            'transactions',
            'reviews_written'
        )