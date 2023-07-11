from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.plates import (PlateListView, PlateDetailView, PlateByLicenseDetailAPIView,
    PlateCapturedListView, PlateCapturedDetailView
)
urlpatterns = format_suffix_patterns([
    path('plate/', PlateListView.as_view()),
    path('plate/<int:pk>/', PlateDetailView.as_view()),
    path('plate/<str:license_plate>/', PlateByLicenseDetailAPIView.as_view()),
    path('plate_captured/', PlateCapturedListView.as_view()),
    path('plate_captured/<int:pk>/', PlateCapturedDetailView.as_view()),
])
