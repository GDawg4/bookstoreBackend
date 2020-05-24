
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
            'age',
            'username'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        print(self.data)
        reader = Reader(email=self.validated_data['email'],
                        name=self.validated_data['name'],
                        lastname=self.validated_data['lastname'],
                        username=self.validated_data['username'],
                        age=self.validated_data['age'])
        password = self.validated_data['password']
        reader.set_password(password)
        reader.save()
        return reader
