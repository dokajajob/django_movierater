from django.contrib import admin

from .models import Items, ItemNumber, Character, Author
from .models import Items, ItemNumber, Author
#from .character import Character


#admin.site.register(Items)

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    #fields = ['title', 'description']
    list_display = ['title', 'description', 'price', 'number', 'authors']
    list_filter = ['published']
    search_fields = ['title', 'price']


admin.site.register(ItemNumber)

admin.site.register(Character)

admin.site.register(Author)