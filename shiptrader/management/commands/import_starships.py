import swapi
from django.core.management.base import BaseCommand
from django.db import models
from shiptrader.models import Starship

class Command(BaseCommand):


    def api_normalize_starship_data(self, starship:swapi.models.Starship):
        normalized_data = {}
        get_model_field = Starship._meta.get_fields()
        for field in get_model_field:
            if not isinstance(field, models.ManyToOneRel):

                api_value = getattr(starship, field.name, None)
                if api_value == 'unknown' or api_value == 'n/a':
                    api_value = None
                elif isinstance(field, models.FloatField) and isinstance(api_value, str):
                    api_value = api_value.replace(",", "")
                elif isinstance(field, models.IntegerField) and isinstance(api_value, str):
                    if "-" in api_value:
                        api_value = api_value.split("-", 1)[1]
                    else:
                        api_value = api_value.replace(",", "")

                normalized_data[field.name] = api_value

        return normalized_data


    def handle(self, *args, **kwargs):
        api_starships = swapi.get_all("starships").items
        obj = Starship.objects.bulk_create(
            Starship(**self.api_normalize_starship_data(starship))
            for starship in api_starships
        )
        self.stdout.write(self.style.SUCCESS(f"Created {len(obj)} objects"))