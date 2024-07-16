from rest_framework import serializers
from tickets.models import Guest, Movie, Reservation, Post, Rating

class MovieSerializer(serializers.ModelSerializer):
    average_rating =serializers.FloatField()
    class Meta:
        model = Movie
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = ['pk', 'reservation', 'name', 'mobile']
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

