from rest_framework import serializers
from plate.models import PlateModel, PlateCapturedModel


class PlateSerializer(serializers.ModelSerializer):
    """
    Serializer for PlateModel
    """
    class Meta:
        model = PlateModel
        fields = [
            'id',
            'user',
            'license_plate',
            'brand',
            'color',
            'status',
            'description',
            'image',
            'created_at',
            'updated_at',
        ]


class PlateCapturedSerializer(serializers.ModelSerializer):
    """
    Serializer for PlateCapturedModel
    """
    class Meta:
        model = PlateCapturedModel
        fields = [
            'id',
            'plate',
            'image_license',
            'image_car',
            'created_at',
            'updated_at',
        ]
