from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

from api.views import MovieViewSet, RatingViewSet, UserViewSet, SearchUserViewSet, AnotherFirst

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)
router.register('usersearch', SearchUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test', AnotherFirst.as_view())
]
