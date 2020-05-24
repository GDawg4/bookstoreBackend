
from rest_framework import serializers

from users.models import Reader


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = (
            'id',
            'name',
            'lastname',
            'email',
            'password',
            'age'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        reader = Reader(email=self.validated_data['email'])
        password = self.validated_data['password']
        reader.set_password(password)
        reader.save()
        return reader
