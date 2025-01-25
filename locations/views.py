from rest_framework import viewsets
from .models import Locations
from .serializers import LocationsSerializer

class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all().order_by('id')
    serializer_class = LocationsSerializer
