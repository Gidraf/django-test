from rest_framework import serializers
from .models import Movie


class MoviesSerializer(serializers.Serializer):
    Title = serializers.CharField()
    Year = serializers.CharField()
    imdbID = serializers.CharField()
    Type = serializers.CharField()
    Poster = serializers.CharField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)