from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'book'

router = SimpleRouter()
router.register('books', views.BookSerializerView)
router.register('authors', views.AuthorSerializerView)

urlpatterns = [
    path('', include(router.urls))
]
