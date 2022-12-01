from django_filters import FilterSet, DateTimeFromToRangeFilter, CharFilter, NumberFilter
from django.db.models import Q

from users.models import NormalUser

class NormalUserFilterSet(FilterSet):

    email = CharFilter(field_name="email", lookup_expr="icontains")
    role = NumberFilter(field_name="role")
    created_at = DateTimeFromToRangeFilter()
    name = CharFilter(method="filter_by_name", lookup_expr="icontains")

    def filter_by_name(self, queryset, name, value):
        return queryset.filter(Q(first_name__icontains=value) | Q(last_name__icontains=value))
    class Meta:
        model = NormalUser
        fields = ['email', 'role', 'created_at']
