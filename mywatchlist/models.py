from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.IntegerField(null=True, blank=True, default=None)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    review = models.TextField(null=True, blank=True)
