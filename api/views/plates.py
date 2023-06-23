from rest_framework import generics
from rest_framework import permissions

from plate.models import PlateModel
from api.serializers.plates import PlateSerializer

class PlateListView(generics.ListCreateAPIView):
    """
    List all plates, or create a new plate.
    """
    queryset = PlateModel.objects.all()
    serializer_class = PlateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PlateDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a plate instance.
    """
    queryset = PlateModel.objects.all()
    serializer_class = PlateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
