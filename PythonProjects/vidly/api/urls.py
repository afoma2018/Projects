from django.urls import path, include
from tastypie.api import Api
from .models import MovieResource

# v1_api = Api(api_name='v1')
# v1_api.register(MovieResource())
movie_resource = MovieResource()

urlpatterns = [
    path('', include(movie_resource.urls))

]
