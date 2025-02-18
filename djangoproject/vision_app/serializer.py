from rest_framework import serializers
from vision_app.models import nodes_model,realtimes_model,image_model



class realtimes_serializer(serializers.ModelSerializer):
    # node=nodes_serializer(many=True,read_only=True,required=False)
    # Date_time=serializers.DateTimeField(format=rf'%d-%m-%y %H:%M')
    class Meta:
        model=realtimes_model
        fields='__all__'
        excludes=['id']


class nodes_serializer(serializers.ModelSerializer):
    realtimes_data=realtimes_serializer(many=True,read_only=True,required=False)

    class Meta:
        model=nodes_model
        fields=['node_id','GPS_Koordinat','Merk','type','zona_instalasi','isolasi','realtimes_data']

class image_serializer(serializers.ModelSerializer):
    class Meta:
        model=image_model
        fields=['photo','node','uploaded_at']

