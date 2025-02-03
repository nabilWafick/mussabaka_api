from rest_framework import viewsets
from rest_framework.response import Response
from .models import Jury
from .serializers import JurySerializer


class JuryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Jury.objects.all()
        serializer = JurySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = JurySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Jury.objects.get(pk=pk)
        except Jury.DoesNotExist:
            return Response(status=404)
        serializer = JurySerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Jury.objects.get(pk=pk)
        except Jury.DoesNotExist:
            return Response(status=404)
        serializer = JurySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Jury.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Jury.DoesNotExist:
            return Response(status=404)
