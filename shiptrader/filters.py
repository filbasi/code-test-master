import django_filters
from .models import Listing


class ListingFilter(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(
        fields=(
            ('price', 'price'),
            ('created_at', 'created_at'),
        )
    )
    starship_class = django_filters.AllValuesFilter(field_name='ship_type__starship_class', label="Type of the starship")