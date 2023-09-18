from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'book'

router = SimpleRouter()
router.register('books/api', views.BookSerializerView)
router.register('authors/api', views.AuthorSerializerView)

urlpatterns = [
    path('', include(router.urls)),

    path('api/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('api/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),

    path('api/token/verify/',
         TokenVerifyView.as_view(),
         name='token_verify'),
]
