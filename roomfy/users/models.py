from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    post1 = models.ImageField(upload_to='profile_posts/', blank=True, null=True)
    post2 = models.ImageField(upload_to='profile_posts/', blank=True, null=True)  # New field for post2
    post3 = models.ImageField(upload_to='profile_posts/', blank=True, null=True)  # New field for post2
    birthday = models.DateField(blank=True, null=True)
    favorite_music = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    link1 = models.TextField(blank=True, null=True)
    link2 = models.TextField(blank=True, null=True)
    link3 = models.TextField(blank=True, null=True)
    link4 = models.TextField(blank=True, null=True)
    social_links = models.JSONField(default=list, blank=True, null=True)  # Store links as a list of dicts
    favorite_books = models.TextField(blank=True, null=True)
    favorite_movies = models.TextField(blank=True, null=True)
    favorite_food = models.TextField(blank=True, null=True)
    room_background = models.CharField(
        max_length=7, 
        blank=True, 
        null=True, 
        default="#a8c7ff"  # Default color
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
