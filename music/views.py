from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from airvinyl.utils.general import StandardPagination
from airvinyl.utils.views import ReadWriteViewMixin
from music.filters import AlbumFilterSet
from music.models import Album, Genre, SubGenre
from music.serializers import AlbumReadSerializer, AlbumWriteSerializer, GenreSerializer, SubGenreSerializer
from users.models import AuthUser
from users.permissions import IsArtist, IsSuperAdmin
from rest_framework.permissions import IsAuthenticated

class GenreAPIView(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))

class SubGenreAPIView(viewsets.ModelViewSet):
    serializer_class = SubGenreSerializer
    queryset = SubGenre.objects.all()
    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))

class AlbumAPIView(viewsets.ModelViewSet, ReadWriteViewMixin):
    read_serializer = AlbumReadSerializer
    write_serializer = AlbumWriteSerializer
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'release_date', 'genre']
    filterset_class = AlbumFilterSet
    # queryset = Album.objects.all()
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['partial_update', 'destroy']:
            self.permission_classes = [IsArtist]
        return super().get_permissions()
    
    def get_queryset(self):
        if self.request.user == AuthUser.ARTIST:
            return Album.objects.filter(auth_user__id=self.request.user.id)
        return Album.objects.filter()
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))