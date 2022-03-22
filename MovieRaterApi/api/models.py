from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360, blank=True)

    def num_of_ratings(self):
         ratings = Rating.objects.filter(movie=self)
         return len(ratings)

    def avg_of_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            print(rating.stars)
            sum += rating.stars

            if len(ratings) > 0:
              return sum / len(ratings)
            else:
              return 0


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    stars = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5)])


    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)


# class User(models.Model):
#     username = models.CharField
