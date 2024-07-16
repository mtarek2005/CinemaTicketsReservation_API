from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User



# Guest -- Movie -- Reservation 

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    #date = models.DateField()
    @property
    def average_rating(self):
        return Rating.objects.filter(movie=self).all().aggregate(models.Avg("rating",default=0)).get('rating__avg')


class Guest(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE )
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE )


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()

class Rating(models.Model):
    author = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE )
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE )
    rating = models.FloatField()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
