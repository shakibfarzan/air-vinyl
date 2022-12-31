from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from airvinyl.utils.general import StandardPagination
from airvinyl.utils.views import ReadWriteViewMixin
from music.filters import AlbumFilterSet
from music.models import Album, Artist, Genre, SubGenre
from music.serializers import AlbumReadSerializer, AlbumWriteSerializer, ArtistReadSerializer, ArtistWriteSerializer, GenreSerializer, SubGenreSerializer
from users.models import AuthUser
from users.permissions import IsSuperAdminOrReadOnly, IsSuperAdmin
from music.permissions import IsArtist
from rest_framework.permissions import IsAuthenticated

class GenreAPIView(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsSuperAdminOrReadOnly]
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))

class SubGenreAPIView(viewsets.ModelViewSet):
    serializer_class = SubGenreSerializer
    queryset = SubGenre.objects.all()
    permission_classes = [IsSuperAdminOrReadOnly]
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))

class AlbumAPIView(viewsets.ModelViewSet, ReadWriteViewMixin):
    read_serializer = AlbumReadSerializer
    write_serializer = AlbumWriteSerializer
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'release_date', 'genre']
    filterset_class = AlbumFilterSet

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsArtist]
        return super().get_permissions()
    
    def get_queryset(self):
        if self.request.user == AuthUser.ARTIST:
            return Album.objects.filter(auth_user__id=self.request.user.id)
        return Album.objects.filter()
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))

class ArtistAPIView(viewsets.ModelViewSet, ReadWriteViewMixin):
    read_serializer = ArtistReadSerializer
    write_serializer = ArtistWriteSerializer    
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'monthy_listeners']
    queryset = Artist.objects.all()
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsArtist | IsSuperAdmin]
        return super().get_permissions()
    
    def get_queryset(self):
        if self.request.user == AuthUser.ARTIST:
            return Artist.objects.filter(auth_user__id=self.request.user.id)
        return Artist.objects.filter()
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))