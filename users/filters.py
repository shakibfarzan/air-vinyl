from django_filters import FilterSet, DateTimeFromToRangeFilter, CharFilter, NumberFilter
from django.db.models import Q, Value
from django.db.models.functions import Concat

from users.models import NormalUser

class NormalUserFilterSet(FilterSet):
    email = CharFilter(field_name="email", lookup_expr="icontains")
    created_at = DateTimeFromToRangeFilter()
    name = CharFilter(method="filter_by_name", lookup_expr="icontains")

    def filter_by_name(self, queryset, name, value):
        queryset = NormalUser.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
        return queryset.filter(Q(full_name__icontains=value))
    class Meta:
        model = NormalUser
        fields = ['email', 'created_at']
