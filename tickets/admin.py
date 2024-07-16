from django.contrib import admin
from .models import Movie, Guest, Reservation, Post, Rating

admin.site.register(Movie)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Post)
admin.site.register(Rating)
