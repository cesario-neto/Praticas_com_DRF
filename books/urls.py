from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'book'

router = SimpleRouter()
router.register('book', views.BookSerializerView)
print(router.urls)

urlpatterns = [
    path('', include(router.urls))
]
