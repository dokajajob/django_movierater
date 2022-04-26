from django.db import models
#from .character import Character


class ItemNumber(models.Model):
    number_10 = models.CharField(max_length=10, blank=True)
    number_13 = models.CharField(max_length=13, blank=True)


class Items (models.Model):
    BOOKS = ('HB', 'Hobbit'), ('LOTR', 'Lord if the Rings')
    STATUSES = (0, 'Unknown'), (1, 'Processed'), (2, 'Paid')
    title = models.CharField(blank=False, unique=True, max_length=36)
    price = models.DecimalField(blank=True, default=0, max_digits=9, decimal_places=2)
    description = models.TextField(blank=True, max_length=256)
    cover = models.ImageField(upload_to='covers/', blank=True)
    published = models.BooleanField(default=False)
    number = models.OneToOneField(ItemNumber, null=True, blank=True, on_delete=models.CASCADE)
    #characters = models.ManyToOneRel(Character, null=True, blank=True, on_delete=models.CASCADE())

def  __str__(self):
    return self.title


class Character(models.Model):
    name = models.CharField(max_length=30)
    items = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='characters')


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    items = models.ManyToManyField(Items, related_name='authors')

class Movies(models.Model):
    name = models.CharField(max_length=30)
    rating = models.DecimalField(max_digits=9, decimal_places=2)

