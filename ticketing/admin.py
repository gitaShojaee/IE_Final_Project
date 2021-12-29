from django.contrib import admin
from .models import Movie, Cinema, ShowTime

# Register your models here.
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(ShowTime)