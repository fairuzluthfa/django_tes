from rest_framework import serializers
from image_app.models import ImageUpload


class image_serializer(serializers.ModelSerializer):
    class Meta:
        model=ImageUpload
        fields='__all__'