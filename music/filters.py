from django_filters import FilterSet, DateTimeFromToRangeFilter, CharFilter, NumberFilter

from music.models import Album

class AlbumFilterSet(FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains")
    genre = CharFilter(field_name="genre")
    released_date = DateTimeFromToRangeFilter()

    class Meta: 
        model = Album
        fields = ['title', 'genre', 'released_date']