from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Book


class BookSerializerView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
