from rest_framework import serializers

from plate.models import PlateModel

class PlateSerializer(serializers.ModelSerializer):
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
            'created_date',
            'image',
        ]
