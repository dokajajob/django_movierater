
from rest_framework import viewsets
from .models import Movies
from .serializer import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movies.objects.all()