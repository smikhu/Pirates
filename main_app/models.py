from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Film(models.Model):
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    plot = models.TextField(max_length=500)
    director = models.CharField(max_length=100)
    rated = models.CharField(max_length=100)
    released = models.CharField(max_length=100)
    metascore = models.CharField(max_length=100)
    imdbrating = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=250) 
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.film.title)

class Rating(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default = 0,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    comment = models.TextField(max_length=250)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="ratings")

    def __str__(self):
        return str(self.pk)
