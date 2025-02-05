from django.contrib import admin
from iot_app.models import SensorData,Device
# Register your models here.

admin.site.register(Device)
admin.site.register(SensorData)
