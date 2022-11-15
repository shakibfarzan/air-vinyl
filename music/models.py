from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
# from users.models import Artist, AuthUser

class Genre(models.Model):
    """Genre class in the system"""
    name = models.CharField(max_length=255)

class SubGenre(models.Model):
    """Subgenre class in the system"""
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
class Album(models.Model):
    """Album class in the system"""
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT)
    album_cover = models.ImageField()
    released_date = models.DateField()
    duration = models.IntegerField()
    
class Track(models.Model):
    """Track class in the system"""
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT, null=True)
    played_count = models.IntegerField(default=0)
    duration = models.IntegerField()
    released_date = models.DateField()
    cover = models.ImageField()
    sub_genre = models.ForeignKey(SubGenre, on_delete=models.RESTRICT)
    artists = models.ManyToManyField(settings.ARTIST_MODEL)
    
class LikeTrack(models.Model):
    """Like track class in the system"""
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class LikeAlbum(models.Model):
    """Like album class in the system"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Playlist(models.Model):
    """Playlist class in the system"""
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    duration = models.IntegerField()
    private = models.BooleanField()
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL)
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    

    