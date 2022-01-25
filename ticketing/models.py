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
    poster = models.ImageField(upload_to='movie_posters/')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
    Represents a cinema (movie theater)
    """
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    capacity = models.IntegerField()
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField()
    image = models.ImageField(upload_to='cinema_images/', null=True)

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    """
    Represents a movie show in a cinema at a specific time
    """
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
        (SALE_OPEN, 'Sale is Open'),
        (TICKETS_SOLD, 'Tickets sold'),
        (SALE_CLOSED, 'Sale Closed'),
        (MOVIE_PLAYED, 'Movie played'),
        (SHOW_CANCELED, 'Show canceled'),
    )
    status = models.IntegerField(choices=status_choices, default=SALE_NOT_STARTED)

    def get_price_display(self):
        return '{}'.format(self.price)

    def is_full(self):
        """
        Returns True if all seats are sold
        """
        return self.free_seats == 0

    def open_sale(self):
        """
        Opens ticket sale
        If sale was opened before, raises an exception
        """
        if self.status == ShowTime.SALE_NOT_STARTED:
            self.status = ShowTime.SALE_OPEN
            self.save()
        else:
            raise Exception('Sale has been started before')

    def close_sale(self):
        """
        Closes ticket sale
        If sale is not open, raises an exception
        """
        if self.status == ShowTime.SALE_OPEN:
            self.status = ShowTime.SALE_CLOSED
            self.save()
        else:
            raise Exception('Sale is not open')

    def expire_showtime(self, is_canceled=False):
        """
        Expires showtime and updates the status
        :param is_canceled: A boolean indicating whether the show is canceled or not, default is False
        """
        if self.status not in (ShowTime.MOVIE_PLAYED, ShowTime.SHOW_CANCELED):
            self.status = ShowTime.SHOW_CANCELED if is_canceled else ShowTime.MOVIE_PLAYED
            self.save()
        else:
            raise Exception('Show has been expired before')

    def reserve_seats(self, seat_count):
        """
        Reserves one or more seats for a customer
        :param seat_count: An integer as the number of seats to be reserved
        """
        assert isinstance(seat_count, int) and seat_count > 0, 'Number of seats should be a positive integer'
        assert self.status == ShowTime.SALE_OPEN, 'Sale is not open'
        assert self.free_seats >= seat_count, 'Not enough free seats'
        self.free_seats -= seat_count
        if self.free_seats == 0:
            self.status = ShowTime.TICKETS_SOLD
        self.save()

    def __str__(self):
        return self.movie.name + " (" + self.cinema.name + ")"


class Ticket(models.Model):
    """
    Represents one or more tickets, bought by a user in an order
    """
    showtime = models.ForeignKey('ShowTime', on_delete=models.PROTECT)
    customer = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT)
    seat_count = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.showtime.__str__()
