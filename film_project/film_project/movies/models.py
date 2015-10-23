from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    country = models.CharField(max_length=30)
    release_date_world = models.DateField()
    release_date_uzb = models.DateField()
    description = models.TextField(max_length=400)
    IMDB = models.FloatField()
    rating = models.FloatField()
    age_restriction = models.IntegerField()
    duration = models.IntegerField()


    # Janr, Persons, comments, reviews boglash kere
    # Nado obsudit'

