from rest_framework import viewsets
from rest_framework.response import Response
from .models import Categories
from .serializers import CategoriesSerializer

class CategoriesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Categories.objects.all()
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Categories.objects.get(pk=pk)
        except Categories.DoesNotExist:
            return Response(status=404)
        serializer = CategoriesSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Categories.objects.get(pk=pk)
        except Categories.DoesNotExist:
            return Response(status=404)
        serializer = CategoriesSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Categories.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Categories.DoesNotExist:
            return Response(status=404)