from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Rating
from django.db.models import Avg
from django.views.generic import ListView, DetailView, View


def home(request):
    movies = Movie.objects.all()
    movie_ratings = {}
    for movie in movies:
        rating = Rating.objects.filter(movie=movie).aggregate(Avg('stars'))
        movie_ratings[movie.movie_title] = rating
    context = {
        'movies': movies,
        'movie_ratings': movie_ratings
    }

    return render(request, 'moviapi/home2.html', context)


class MovieListView(ListView):
    model = Movie
    template_name = 'moviapi/home2.html'
    context_object_name = 'movies'

    paginate_by = 6


class MovieDetailView(DetailView):
    model = Movie


class RatingView(View):
    def get(self, request):
        movie_instance = Movie.objects.get(movie=['movie'])
        ratings = Rating.objects.filter(movie=movie_instance)
        context = {'movies': movie_instance, 'ratings': ratings}
        return render(request, 'moviapi/home2.html', context)


def about(request):
    return render(request, 'moviapi/about.html', {'title': 'About'})


def description(request):
    return render(request, 'moviapi/movie_detail.html', {'title': 'Description {{ movie.movie_title }}'})
