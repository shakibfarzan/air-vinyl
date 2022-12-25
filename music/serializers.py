from rest_framework import serializers
from airvinyl.utils.serializers import ResponseSerializer
from .models import Album, Genre, SubGenre


class GenreSerializer(serializers.ModelFieldSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class SubGenreSerializer(serializers.ModelFieldSerializer):
    genre = GenreSerializer()
    class Meta:
        model = SubGenre
        fields = '__all__'

class AlbumReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = Album.READ_FIELDS
        
class AlbumWriteSerializer(ResponseSerializer):
    response_serializer = AlbumReadSerializer
    genre = serializers.PrimaryKeyRelatedField(required=True, queryset=Genre.objects.all())
    class Meta:
        model = Album
        fields = Album.WRITE_FIELDS
