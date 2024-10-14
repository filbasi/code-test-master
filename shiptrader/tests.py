from rest_framework.test import APITestCase
from .models import Listing, Starship
from model_mommy import mommy
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class CreateAPIViewAPITestCase(APITestCase):

    def test_starship_list(self):
        quantity = 2
        mommy.make('shiptrader.Starship', _quantity=quantity)
        url = reverse('starship-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), quantity)

    def test_create_listing(self):
        starship = mommy.make('shiptrader.Starship')
        url = reverse('listing-create')
        data = {"name": "test12", "price": 123, "ship_type": starship.id}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Listing.objects.count(), 1)
        obj = Listing.objects.all().first()
        self.assertEqual(obj.name, data['name'])
        self.assertEqual(obj.price, data['price'])
        self.assertEqual(obj.ship_type, starship)

    def test_listing_list(self):
        quantity = 2
        mommy.make('shiptrader.Listing', _quantity=quantity)
        url = reverse('listing-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), quantity)

    def test_listing_update(self):
        listing = mommy.make('shiptrader.Listing', name="previous_listing_name")
        url = reverse('listing-update', args=[listing.id])
        data = {"name": "updated_listing_name"}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(Listing.objects.get(id=listing.id).name, data['name'])