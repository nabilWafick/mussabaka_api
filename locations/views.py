from rest_framework import viewsets
from rest_framework.response import Response
from .models import Locations
from .serializers import LocationsSerializer


class LocationsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Locations.objects.all()
        serializer = LocationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LocationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Locations.objects.get(pk=pk)
        except Locations.DoesNotExist:
            return Response(status=404)
        serializer = LocationsSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Locations.objects.get(pk=pk)
        except Locations.DoesNotExist:
            return Response(status=404)
        serializer = LocationsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Locations.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Locations.DoesNotExist:
            return Response(status=404)
