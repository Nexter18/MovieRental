from typing import List
from django.shortcuts import render
from .models import Movie, Rating
from django.views.generic import ListView, DetailView, View


def home(request):
    movies = Movie.objects.all()
    search_term = {}
    if 'search' in request.GET:
        search_term = request.GET['search']
        movies = movies.filter(description__icontains=search_term)
    context = {'movies': movies, 'search_term': search_term}

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
