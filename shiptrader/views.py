from rest_framework import generics
from .models import Starship, Listing
from .serializers import StarshipSerializer, ListingSerializer
from .filters import ListingFilter


# Create your views here.
class StarshipListAPIView(generics.ListAPIView):
    serializer_class = StarshipSerializer
    queryset = Starship.objects.all()

class ListingAPIView:
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class ListingCreateAPIView(ListingAPIView,generics.CreateAPIView):
    pass

class ListingListAPIView(ListingAPIView, generics.ListAPIView):
    filterset_class = ListingFilter

class ListingUpdateAPIView(ListingAPIView, generics.UpdateAPIView, generics.RetrieveAPIView):
    http_method_names = ['patch', 'get']


