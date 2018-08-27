from django.contrib import admin

# Register your models here.
from ezp10.models import Plant, Capture


class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CaptureAdmin(admin.ModelAdmin):
    list_display = ('plant_id', 'name', )


admin.site.register(Plant, PlantAdmin)
admin.site.register(Capture, CaptureAdmin)
