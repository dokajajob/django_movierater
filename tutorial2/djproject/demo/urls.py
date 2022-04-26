

from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import AnotherFirst, ItemViewSet
from rest_framework import routers

#from .views import ItemViewSet, ItemViewSetPrice
from .views import ItemViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register('items', ItemViewSet)
router.register('movies', MovieViewSet)
#router.register('price', ItemViewSetPrice)

urlpatterns = [
    #path('', views.first),
    path('second', views.second),
    #path('another', AnotherFirst.as_view()),
    path('', include(router.urls)),
    #path('price', include(router.urls)),
]
