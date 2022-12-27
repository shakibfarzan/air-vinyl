from django_filters import FilterSet, DateTimeFromToRangeFilter, CharFilter
from django.db.models import Q
from music.models import Album

class AlbumFilterSet(FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains")
    genre = CharFilter(method="filter_by_genre")
    released_date = DateTimeFromToRangeFilter()

    def filter_by_genre(self, queryset, name, value):
        return queryset.filter(Q(genre__name=value))
    class Meta: 
        model = Album
        fields = ['title', 'genre', 'released_date']