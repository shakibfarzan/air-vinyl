from rest_framework import serializers
from airvinyl.utils.serializers import ResponseSerializer
from .models import Album, Genre, SubGenre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class SubGenreSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    class Meta:
        model = SubGenre
        fields = '__all__'

class AlbumReadSerializer(serializers.ModelSerializer):
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
