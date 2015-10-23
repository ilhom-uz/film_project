from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    movies_list = Movie.objects.all()
    context = {'movies_list': movies_list}
    return render(request, 'movies/index.html', context)

    return HttpResponse(output)
def detail(request, movie_id):
    movie_detail = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'Movie': movie_detail})