from rest_framework import viewsets

from authors.models import Author
from authors.serializers import AuthorSerializer
# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer