from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ticketing.models import Movie, Cinema


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return HttpResponse(context['movies'])


def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas': cinemas
    }
    return HttpResponse(context['cinemas'])


def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {
        'movie': movie
    }
    return HttpResponse(context['movie'])


def cinema_details(request, cinema_id):
    cinema = Cinema.objects.get(pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return HttpResponse(context['cinema'])