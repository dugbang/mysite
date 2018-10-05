from django.contrib import admin

# Register your models here.
from ezp10.models import Plant, Capture, Controller, Report


class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')


class ControllerAdmin(admin.ModelAdmin):
    list_display = ('serial', 'is_active', 'plant',
                    'minute_of_action_cycle', 'minute_of_upload_cycle',
                    'iis_tank_capacity', 'iis_temperature', 'iis_ph', 'iis_mc',
                    'iis_temp_humidity_high', 'iis_temp_humidity_low', 'iis_luminance', 'iis_co2',
                    'ois_led', 'ois_pump', 'ois_pan_high', 'ois_pan_low',
                    'is_usb_camera', 'modify_date', 'actuator_csv',
                    'capture_times', 'stable_time_of_camera')


# class ActuatorAdmin(admin.ModelAdmin):
#     list_display = ('controller', 'upload')


class CaptureAdmin(admin.ModelAdmin):
    list_display = ('plant', 'controller', 'image', 'create_at')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('plant', 'controller', 'create_at',
                    'tank_capacity', 'temperature', 'ph', 'mc',
                    'temp_humidity_high', 'temp_humidity_low', 'luminance', 'co2',
                    'on_off_led', 'on_off_pump', 'on_off_pan_high', 'on_off_pan_low',
                    )


admin.site.register(Plant, PlantAdmin)
admin.site.register(Controller, ControllerAdmin)
# admin.site.register(Actuator, ActuatorAdmin)
admin.site.register(Capture, CaptureAdmin)
admin.site.register(Report, ReportAdmin)
