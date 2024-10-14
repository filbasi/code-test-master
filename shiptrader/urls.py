from django.conf.urls import url
from .views import StarshipListAPIView, ListingCreateAPIView, ListingListAPIView, ListingUpdateAPIView


urlpatterns = [
    url('^starship/$', StarshipListAPIView.as_view(), name="starship-list"),
    url('^listing/create/$', ListingCreateAPIView.as_view(), name="listing-create"),
    url('^listing/list/$', ListingListAPIView.as_view(), name="listing-list"),
    url('^listing/update/(?P<pk>\d+)/$', ListingUpdateAPIView.as_view(), name="listing-update"),
]