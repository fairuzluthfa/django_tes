from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from iot_app.models import Device,SensorData
from iot_app.serializers import DeviceSerializer,SensorDataSerializer
from datetime import datetime


# GET /api/devices/ - List all devices
# POST /api/devices/ - Register new device
# GET /api/devices/{device_id}/ - Get device details
# PUT /api/devices/{device_id}/ - Update device
# POST /api/devices/{device_id}/upload_data/ - Upload sensor data
# GET /api/devices/{device_id}/latest_data/ - Get latest sensor data

# Create your views here.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer
    lookup_field='device_id'     #next url key

    @action(detail=True, methods=['post'])
    def upload_data(self, request, device_id=None):
        try:
            device = self.get_object()
            sensor_data = SensorData(
                device=device,
                temperature=request.data.get('temperature'),
                humidity=request.data.get('humidity')
            )
            sensor_data.save()
            return Response(SensorDataSerializer(sensor_data).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action (detail=True,methods=['get'])
    def latest_data(self,request,device_id=None):
        device=self.get_object()
        sensor_data=device.sensor_data.first()
        if sensor_data:
            return Response(SensorDataSerializer(sensor_data).data)
        return Response({'message':'No data available'},status=status.HTTP_404_NOT_FOUND)
    
    # @action (detail=True,methods=['get'])
    # def all_data(self,request,device_id=None):
    #     device=self.get_object()
    #     sensor_data=device.sensor_data.all()
    #     if sensor_data:
    #         return Response(SensorDataSerializer(sensor_data,many=True).data)
    #     return Response({'message':'No data available'},status=status.HTTP_404_NOT_FOUND)
    
    
    @action(detail=True, methods=['get'])
    def all_data(self, request, device_id=None):
        device = self.get_object()
        sensor_data = device.sensor_data1.all()

        # Get query parameters for date filtering
        start_date = request.query_params.get('start_date')  # e.g., "2025-02-01T00:00:00"
        end_date = request.query_params.get('end_date')  # e.g., "2025-02-03T23:59:59"

        if start_date:
            try:
                start_date = datetime.fromisoformat(start_date)
                sensor_data = sensor_data.filter(timestamp__gte=start_date)
            except ValueError:
                return Response({'error': 'Invalid start_date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)'}, 
                                status=status.HTTP_400_BAD_REQUEST)

        if end_date:
            try:
                end_date = datetime.fromisoformat(end_date)
                sensor_data = sensor_data.filter(timestamp__lte=end_date)
            except ValueError:
                return Response({'error': 'Invalid end_date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)'}, 
                                status=status.HTTP_400_BAD_REQUEST)

        if sensor_data.exists():
            return Response(SensorDataSerializer(sensor_data, many=True).data)
        
        return Response({'message': 'No data available for the given date range'}, 
                        status=status.HTTP_404_NOT_FOUND)

    # GET /iot/devices/tes1/all_data/?start_date=2025-02-01T00:00:00&end_date=2025-02-03T23:59:59

