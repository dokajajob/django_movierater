from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),

]