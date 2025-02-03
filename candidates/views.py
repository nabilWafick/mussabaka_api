from rest_framework import viewsets
from rest_framework.response import Response
from .models import Candidates
from .serializers import CandidatesSerializer


class CandidatesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Candidates.objects.all()
        serializer = CandidatesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CandidatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Candidates.objects.get(pk=pk)
        except Candidates.DoesNotExist:
            return Response(status=404)
        serializer = CandidatesSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Candidates.objects.get(pk=pk)
        except Candidates.DoesNotExist:
            return Response(status=404)
        serializer = CandidatesSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Candidates.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Candidates.DoesNotExist:
            return Response(status=404)
