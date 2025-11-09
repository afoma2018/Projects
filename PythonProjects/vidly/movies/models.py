from django.db import models
from django.utils import timezone

# Create your models here.


class Genere(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
