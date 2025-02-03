from rest_framework import viewsets
from rest_framework.response import Response
from .models import Contests
from .serializers import ContestsSerializer


class ContestsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Contests.objects.all()
        serializer = ContestsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ContestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Contests.objects.get(pk=pk)
        except Contests.DoesNotExist:
            return Response(status=404)
        serializer = ContestsSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Contests.objects.get(pk=pk)
        except Contests.DoesNotExist:
            return Response(status=404)
        serializer = ContestsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Contests.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Contests.DoesNotExist:
            return Response(status=404)
