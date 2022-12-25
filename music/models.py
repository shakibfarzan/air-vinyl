from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from users.models import AuthUser

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
    
    READ_FIELDS = ['id', 'title', 'genre', 'album_cover', 'released_date', 'duration']
    WRITE_FIELDS = ['title', 'genre', 'album_cover']
    REQUIRED_FIELDS = ['title', 'genre']

class Artist(AuthUser):
    """Artist class in the system"""
    name = models.CharField(max_length=255)
    albums = models.ManyToManyField(Album)
    auth_user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
        related_name="artist",
        primary_key=True,
        parent_link=True,
    )
    about = models.CharField(max_length=255)
    monthly_listeners = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.role:
            self.role = AuthUser.ARTIST
        super(AuthUser, self).save(*args, **kwargs)
    
class Track(models.Model):
    """Track class in the system"""
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT, null=True)
    played_count = models.IntegerField(default=0)
    duration = models.IntegerField()
    released_date = models.DateField()
    cover = models.ImageField()
    sub_genre = models.ForeignKey(SubGenre, on_delete=models.RESTRICT)
    artists = models.ManyToManyField(Artist)
    
class LikeTrack(models.Model):
    """Like track class in the system"""
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class LikeAlbum(models.Model):
    """Like album class in the system"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Playlist(models.Model):
    """Playlist class in the system"""
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    duration = models.IntegerField()
    private = models.BooleanField()
    owner = models.ManyToManyField(AuthUser)
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
