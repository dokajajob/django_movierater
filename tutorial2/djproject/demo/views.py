from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Items, Movies
#from .serializers import ItemSerializer, ItemSerializerPrice
from .serializers import ItemSerializer, ItemMiniSerializer, MovieSerializer


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemMiniSerializer
    queryset = Items.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ItemSerializer(instance)
        return Response(serializer.data)

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movies.objects.all()
    authentication_classes = (TokenAuthentication,)



# class ItemViewSetPrice(viewsets.ModelViewSet):
#     serializer_class = ItemSerializerPrice
#     queryset = Items.objects.all()





# class AnotherFirst(View):
#
#     #items = Items.objects.all()
#     #items = Items.objects.filter(published=True)
#     items = Items.objects.get(id=2)
#
#     # output = f'There are {len(items)} items'
#     # itemsOutput = ''
#     itemTwo = f'Item with id 2 is : {items.id}'
#     #
#     # for item in items:
#     #     itemsOutput += f'{item.title} id is  {item.id}<br>'
#
#
#     def get(self, request):
#         return HttpResponse(self.itemTwo)
#         #return HttpResponse(self.output)

#
# def first(request):
#     items = Items.objects.all()
#
#     return render(request, 'firstTemplate.html', {'items': items})

def second(request):
    return HttpResponse('Second here')


