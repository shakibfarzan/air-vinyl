from django.urls import path
from airvinyl.utils.general import LIST_CREATE_MODEL_VIEW_SET, DETAIL_MODEL_VIEW_SET
from music.views import AlbumAPIView, ArtistAPIView, GenreAPIView, SubGenreAPIView


urlpatterns = [
    path("genres/", GenreAPIView.as_view(LIST_CREATE_MODEL_VIEW_SET), name="genre"),
    path("genres/<int:pk>/", GenreAPIView.as_view(DETAIL_MODEL_VIEW_SET), name="genre-detail"),
    path("sub-genres/", SubGenreAPIView.as_view(LIST_CREATE_MODEL_VIEW_SET), name="sub-genre"),
    path("sub-genres/<int:pk>/", SubGenreAPIView.as_view(DETAIL_MODEL_VIEW_SET), name="sub-genre-detail"),
    path("albums/", AlbumAPIView.as_view(LIST_CREATE_MODEL_VIEW_SET), name="album"),
    path("albums/<int:pk>/", AlbumAPIView.as_view(DETAIL_MODEL_VIEW_SET), name="album-detail"),
    path("artists/", ArtistAPIView.as_view(LIST_CREATE_MODEL_VIEW_SET), name="artist"),
    path("artists/<int:pk>/", ArtistAPIView.as_view(DETAIL_MODEL_VIEW_SET), name="artist-detail"),
]
