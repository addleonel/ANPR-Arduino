from django.contrib import admin
from plate.models import PlateModel,  PlateCapturedModel


@admin.register(PlateModel)
class PlateAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'license_plate',
        'brand',
        'color',
        'status',
        'description',
        'image',
    )
    search_fields = ('user', 'license', 'brand', 'color', 'status',)
    list_filter = ('user',)


@admin.register(PlateCapturedModel)
class PlateCapturedAdmin(admin.ModelAdmin):
    list_display = (
        'plate',
        'image_license',
        'image_car',
    )
    search_fields = ('plate',)
    list_filter = ('plate',)
