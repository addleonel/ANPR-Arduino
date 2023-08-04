from django.urls import path
from plate.views import home, plate_list

app_name = 'plate'
urlpatterns = [
    path('', home, name='plate_home'),
    path('list/', plate_list, name='plate_list'),
]
