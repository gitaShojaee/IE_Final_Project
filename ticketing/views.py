from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ticketing.models import Movie, Cinema

def home_page(request):
    movies = Movie.objects.order_by('-year').all()[:5]
    cinemas = Cinema.objects.all()
    context = {
        'movies': movies,
        'cinemas' : cinemas,
    }
    return render(request, 'ticketing/homePage.html', context)
def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'ticketing/movie_list.html', context)


def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas': cinemas
    }
    return render(request, 'ticketing/cinema_list.html', context)


def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'ticketing/movie_details.html', context)


def cinema_details(request, cinema_id):
    cinema = Cinema.objects.get(pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request, 'ticketing/cinema_details.html', context)