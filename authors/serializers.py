from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    has_account = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'birth_date',
            'bio',
            'has_account',
            'account_linked',
            'author_pic',
            'books_written'
        )

    def get_has_account(self, obj):
        if obj.has_account:
            return obj.account_linked
        return None