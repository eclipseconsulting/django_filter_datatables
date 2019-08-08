import django_filters

from . import models


class CustomerFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')

    class Meta:
        model = models.Customer
        fields = ['first_name', 'last_name', 'city', 'state', 'zip', 'phone']

