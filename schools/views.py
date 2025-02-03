from rest_framework import viewsets
from rest_framework.response import Response
from .models import Schools
from .serializers import SchoolsSerializer


class SchoolsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Schools.objects.all()
        serializer = SchoolsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SchoolsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Schools.objects.get(pk=pk)
        except Schools.DoesNotExist:
            return Response(status=404)
        serializer = SchoolsSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Schools.objects.get(pk=pk)
        except Schools.DoesNotExist:
            return Response(status=404)
        serializer = SchoolsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Schools.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Schools.DoesNotExist:
            return Response(status=404)
