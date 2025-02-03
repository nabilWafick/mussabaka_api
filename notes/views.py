from rest_framework import viewsets
from rest_framework.response import Response
from .models import Notes
from .serializers import NotesSerializer


class NotesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Notes.objects.all()
        serializer = NotesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            return Response(status=404)
        serializer = NotesSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            return Response(status=404)
        serializer = NotesSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Notes.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Notes.DoesNotExist:
            return Response(status=404)
