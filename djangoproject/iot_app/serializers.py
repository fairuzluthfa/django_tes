from iot_app.models import SensorData,Device
from rest_framework import serializers

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=SensorData
        # fields='__all__'
        fields=['id','temperature','humidity','timestamp']

class DeviceSerializer(serializers.ModelSerializer):
    sensor_data1 = SensorDataSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model=Device
        # fields='__all__'
        # fields=['id','device_id','name','status','last_seen','sensor_data1']
        fields=['id','__all__']