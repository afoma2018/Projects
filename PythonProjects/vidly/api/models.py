from django.db import models
from movies.models import Movie
from tastypie.resources import ModelResource
# Create your models here.


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        allowed_methods = ['get', 'post', 'put', 'delete']
        excludes = ['date_created', 'resource_uri', 'daily_rate']
