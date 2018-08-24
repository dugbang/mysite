from django.contrib import admin

# Register your models here.
from ezp10.models import Plant


class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Plant, PlantAdmin)
