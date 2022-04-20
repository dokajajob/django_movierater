from django.contrib import admin

from api.models import Rating, Movie, Check

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Check)
