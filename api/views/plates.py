from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
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


class PlateByLicenseDetailAPIView(APIView):
    """
    Retrieve and update linkcard
    """
    queryset = PlateModel.objects.all()
    serializer_class = PlateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_plate_object(self, license_plate):
        try:
            return PlateModel.objects.get(license_plate=license_plate)
        except PlateModel.DoesNotExist:
            raise Http404

    def get(self, request, license_plate, format=None):
        plate = self.get_plate_object(license_plate=license_plate)
        serializer = self.serializer_class(instance=plate, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, license_plate, format=None):
        plate = self.get_plate_object(license_plate=license_plate)
        serializer = self.serializer_class(plate, request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, license_plate, format=None):
        plate = self.get_plate_object(license_plate=license_plate)
        serializer = self.serializer_class(plate, request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)