from .serializers import BookSerializer, AuthorSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Book, Author
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookSerializerView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = 'get', 'post', 'head', 'options', 'patch',
    permission_classes = IsAuthenticatedOrReadOnly,


class AuthorSerializerView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = 'get', 'post', 'patch'
    permission_classes = IsAuthenticatedOrReadOnly,
