from django.contrib import admin
from user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'surname',
        'dni',
        'address',
        'email',
        'phone',
        'description_profile',
        'city',
        'country',
        'picture',
    )
    search_fields = ('user', 'name', 'surname', 'dni',
                     'address', 'email', 'phone', 'city', 'country')
    list_filter = ('user',)
