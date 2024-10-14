from rest_framework import serializers
from .models import Starship, Listing
from django.core.exceptions import ValidationError


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = "__all__"

class ListingSerializer(serializers.ModelSerializer):
    ship_type = serializers.SlugRelatedField(slug_field='name', queryset=Starship.objects.all())
    class Meta:
        model = Listing
        fields = "__all__"
    
    def validate_ship_type(self, data):
        obj = Starship.objects.filter(name=data).first()
        if obj is None:
            raise ValidationError(
                f'Invalid starship name "{data}" - object does not exist'
            )
        return obj