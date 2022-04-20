from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'num_of_ratings', 'avg_of_ratings')



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

        # def create(self, validated_data):
        #     user = User.objects.create_user(**validated_data)
        #     Token.objects.create(user=user)
        #     return user

        def create(self, validated_data):
            # user = User(
            #     username=validated_data['username'],
            #     password=validated_data['password']
            # )
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            user.set_password('password')
            user.save()
            return user
