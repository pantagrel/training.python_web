from django.contrib import admin
from plant.models import Plant

class PlantAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'genus', 'species', )
    list_filter = ('common_name', 'genus', )
    ordering = ('common_name', 'genus', 'species', )

admin.site.register(Plant, PlantAdmin)