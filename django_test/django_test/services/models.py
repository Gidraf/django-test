from django.db import models


class Movie(models.Model):
    Title = models.TextField()
    Year = models.TextField()
    imdbID = models.TextField()
    Type = models.TextField()
    Poster = models.TextField()