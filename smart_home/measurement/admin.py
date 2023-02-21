from django.contrib import admin
from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id_sensor', 'id_sensor_description', 'temperature', 'date']

    @admin.display(ordering='id_sensor__description')
    def id_sensor_description(self, obj):
        return obj.id_sensor.description