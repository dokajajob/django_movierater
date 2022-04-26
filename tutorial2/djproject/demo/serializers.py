from rest_framework import serializers

from .models import Items, ItemNumber, Character, Author, Movies


class ItemNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemNumber
        fields = ['id', 'number_10', 'number_13']

class ItemCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']

class ItemAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']


class ItemSerializer(serializers.ModelSerializer):
    number = ItemNumberSerializer(many=False)
    characters = ItemCharacterSerializer(many=True)
    authors = ItemAuthorSerializer(many=True)

    class Meta:
        model = Items
        fields = ['id', 'title', 'description', 'number', 'characters', 'authors']


class ItemMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id', 'title']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['name', 'rating']



# class ItemSerializerPrice(serializers.ModelSerializer):
#     class Meta:
#         model = Items
#         fields = ['price']