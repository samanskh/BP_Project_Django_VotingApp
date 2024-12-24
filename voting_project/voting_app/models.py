# voting_app/models.py

from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='movie_covers/')
    points = models.IntegerField(default=0)

# voting_app/models.py
class Series(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='series_covers/')
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'series'


