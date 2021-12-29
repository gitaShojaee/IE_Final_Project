from django.db import models


# Create your models here.
class Movie(models.Model):
    """
    Represents a movie
    """
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    year = models.IntegerField()
    length = models.IntegerField()
    description = models.TextField()


class Cinema(models.Model):
    """
    Represents a cinema (movie theater)
    """
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    capacity = models.IntegerField()
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField()


class ShowTime(models.Model):
    """
    Represents a movie show in a cinema at a specific time
    """
    # read more about on_delete from
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete
    # choices are PROTECT, CASCADE, SET_NULL, SET_DEFAULT, SET(), DO_NOTHING
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT)
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT)

    start_time = models.DateTimeField()
    price = models.IntegerField()
    salable_seats = models.IntegerField()
    free_seats = models.IntegerField()

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'Sale not started'),
        (SALE_OPEN, 'Sale Open'),
        (TICKETS_SOLD, 'Tickets sold'),
        (SALE_CLOSED, 'sale Closed'),
        (MOVIE_PLAYED, 'Movie played'),
        (SHOW_CANCELED, 'Show canceled'),
    )
    status = models.IntegerField(choices=status_choices, default=SALE_NOT_STARTED)
