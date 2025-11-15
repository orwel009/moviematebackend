from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Movie(models.Model):
    STATUS_CHOICES = [
        ('watching', 'Watching'),
        ('completed', 'Completed'),
        ('wishlist', 'Wishlist'),
    ]

    MEDIA_TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('tv', 'TV Show'),
    ]

    title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=8, choices=MEDIA_TYPE_CHOICES, default='movie')
    director = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=100, blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='wishlist')
    rating = models.FloatField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)

    episodes_watched = models.IntegerField(default=0, blank=True, null=True)
    total_episodes = models.IntegerField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

from django.db import models

class AdminMovie(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('tv', 'TV Show'),
    ]

    title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=8, choices=MEDIA_TYPE_CHOICES, default='movie')
    director = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=100, blank=True, null=True)

    total_episodes = models.IntegerField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
