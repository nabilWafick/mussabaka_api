from rest_framework import viewsets
from rest_framework.response import Response
from .models import Questionnaires
from .serializers import QuestionnairesSerializer


class QuestionnairesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Questionnaires.objects.all()
        serializer = QuestionnairesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = QuestionnairesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Questionnaires.objects.get(pk=pk)
        except Questionnaires.DoesNotExist:
            return Response(status=404)
        serializer = QuestionnairesSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Questionnaires.objects.get(pk=pk)
        except Questionnaires.DoesNotExist:
            return Response(status=404)
        serializer = QuestionnairesSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Questionnaires.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Questionnaires.DoesNotExist:
            return Response(status=404)
