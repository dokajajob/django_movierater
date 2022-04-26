from mongoengine import Document, fields
from django.db import models

class Blogs(Document):
   name = fields.StringField()
   topic = fields.StringField()
   date = fields.DateTimeField()
   addition_info = fields.DictField()


class Movies(models.Model):
   name = models.CharField(max_length=30)
   rating = models.DecimalField(max_digits=9, decimal_places=2)