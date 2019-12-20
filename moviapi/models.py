from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    """docstring for Movie."""
    movie_title = models.CharField(max_length=100)
    trailer = models.URLField(default='https://www.youtube.com/', max_length=200)
    image = models.ImageField(default='movie.jpg', upload_to='movies')
    description = models.TextField()
    category = models.CharField(default='' , max_length=100)
    rentalprice = models.CharField(max_length=10)
    saleprice = models.CharField(max_length=10)
    date_added = models.DateTimeField(default=timezone.now)
    available = models.CharField(max_length=20)

    def __str__(self):
        return self.movie_title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
