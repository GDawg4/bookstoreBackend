from rest_framework import serializers

from authors.models import Author

from books.serializers import BooksSerializer


class AuthorSerializer(serializers.ModelSerializer):
    has_account = serializers.SerializerMethodField()
    books_written = BooksSerializer(many=True)

    class Meta:
        model = Author
        fields = (
            'name',
            'birth_date',
            'has_account',
            'account_linked',
            'books_written'
        )

    def get_has_account(self, obj):
        if obj.has_account:
            return obj.account_linked
        return None
