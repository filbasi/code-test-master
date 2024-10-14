from rest_framework import serializers
from .models import Starship, Listing
from django.core.exceptions import ValidationError


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = "__all__"

class ListingSerializer(serializers.ModelSerializer):
    ship_type = serializers.CharField(required=True)
    # import pdb; pdb.set_trace()
    # ship_type = serializers.PrimaryKeyRelatedField(queryset=Starship.objects.all())
    class Meta:
        model = Listing
        fields = "__all__"

    # def validate_ship_type(self, data):
    #     import pdb; pdb.set_trace()
    #     obj = Starship.objects.filter(name=data).first()
    #     if obj is None:
    #         raise ValidationError(
    #             f'Invalid ship name "{data}" - object does not exist'
    #         )
    #     return obj