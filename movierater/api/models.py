from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)


class Rating(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), 
                                            MaxValueValidator(5)])
    
    class Meta:

        unique_together = (("user", "movie"),)
        indexes = [
            models.Index(fields=["user", "movie"]),
        ]
