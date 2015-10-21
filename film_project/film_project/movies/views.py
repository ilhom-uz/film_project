from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    movies_list = Movie.objects.all()
    context = {'movies_list': movies_list}
    return render(request, 'movies/index.html', context)