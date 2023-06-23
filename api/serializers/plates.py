from rest_framework import serializers

from plate.models import Plate

class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = [
            'id',
            'user',
            'license_plate',
            'brand',
            'color',
            'description',
            'created_date',
            'image',
        ]
