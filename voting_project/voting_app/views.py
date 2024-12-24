
from .models import Movie, Series
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'home.html')

def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def vote(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.points += 1
    movie.save()
    return render(request, 'vote.html', {'movie': movie})

def ratings(request):
    movies = Movie.objects.all()
    series = Series.objects.all()
    return render(request, 'ratings.html', {'movies': movies, 'series': series})

# voting_app/views.py

def series(request):
    series = Series.objects.all()
    return render(request, 'series.html', {'series': series})

def vote_series(request, series_id):
    serie = get_object_or_404(Series, pk=series_id)
    serie.points += 1
    serie.save()
    return render(request, 'vote_series.html', {'serie': serie})
