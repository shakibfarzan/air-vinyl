from rest_framework import serializers
from airvinyl.utils.serializers import ResponseSerializer
from users.serializers import AuthUserReadSerializer, AuthUserWriteSerializer
from .models import Album, Artist, Genre, SubGenre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class SubGenreSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    class Meta:
        model = SubGenre
        fields = '__all__'

class ArtistReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = AuthUserReadSerializer.Meta.fields + Artist.READ_FIELDS
        
class ArtistWriteSerializer(ResponseSerializer):
    response_serializer = ArtistReadSerializer
    class Meta:
        model = Artist
        fields = AuthUserWriteSerializer.Meta.fields + Artist.WRITE_FIELDS        
        
class AlbumReadSerializer(serializers.ModelSerializer):
    artist = ArtistReadSerializer(many=True, read_only=True)
    genre = GenreSerializer()
    class Meta:
        model = Album
        fields = '__all__'
        
class AlbumWriteSerializer(ResponseSerializer):
    response_serializer = AlbumReadSerializer
    genre = serializers.PrimaryKeyRelatedField(required=True, queryset=Genre.objects.all())
    class Meta:
        model = Album
        fields = Album.WRITE_FIELDS