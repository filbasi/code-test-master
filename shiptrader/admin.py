from django.contrib import admin
from .models import Starship, Listing

# Register your models here.

class StarshipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Starship, StarshipAdmin)

class ListingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listing, ListingAdmin)
