from rest_framework import viewsets
from rest_framework.response import Response
from .models import Results
from .serializers import ResultsSerializer


class ResultsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Results.objects.all()
        serializer = ResultsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ResultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Results.objects.get(pk=pk)
        except Results.DoesNotExist:
            return Response(status=404)
        serializer = ResultsSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Results.objects.get(pk=pk)
        except Results.DoesNotExist:
            return Response(status=404)
        serializer = ResultsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Results.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Results.DoesNotExist:
            return Response(status=404)
