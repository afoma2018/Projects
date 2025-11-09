from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie

# Create your views here.


def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    movies = Movie.objects.all()
    # one_movie = Movie.objects.filter(id=1)
    return render(request, "movies/index.html", {'movies': movies})
    # return HttpResponse(movie_out)


def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'movies/detail.html', {'movie': movie})

    # try:
    #     movie = Movie.objects.get(pk=id)
    # except Movie.DoesNotExist:
    #     raise Http404('movie not found')
    # return render(request, "movies/movie_detail.html", {"movie": movie})
