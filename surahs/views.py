from rest_framework import viewsets
from rest_framework.response import Response
from .models import Surahs
from .serializers import SurahsSerializer


class SurahsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Surahs.objects.all()
        serializer = SurahsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SurahsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Surahs.objects.get(pk=pk)
        except Surahs.DoesNotExist:
            return Response(status=404)
        serializer = SurahsSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Surahs.objects.get(pk=pk)
        except Surahs.DoesNotExist:
            return Response(status=404)
        serializer = SurahsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Surahs.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Surahs.DoesNotExist:
            return Response(status=404)
