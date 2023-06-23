from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.plates import PlateList, PlateDetail

urlpatterns = format_suffix_patterns([
    path('api/plate/', PlateList.as_view()),
    path('api/plate/<int:pk>/', PlateDetail.as_view()),
])
