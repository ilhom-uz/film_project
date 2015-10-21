from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    country = models.CharField(max_length=30)
    release_date_world = models.DateField()
    release_date_uzb = models.DateField()
    description = models.TextField(max_length=400)
    IMDB = models.DecimalField(max_length=4)
    rating = models.DecimalField(max_length=4)
    age_restriction = models.IntegerField()
    duration = models.TimeField()

    # Janr, Persons, comments, reviews boglash kere
    # Nado obsudit'

