from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 100)
    published_in_year = models.IntegerField()
    total_in_stock = models.IntegerField()
    recommended_by = models.ForeignKey(User)



