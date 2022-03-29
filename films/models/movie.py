from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    year = models.DateField(null=False, blank=False)
    imdb = models.FloatField()
    genre = models.CharField(max_length=256)
    actor = models.ManyToManyField(to='films.actor')

    class Meta:
        db_table = "Movie"
