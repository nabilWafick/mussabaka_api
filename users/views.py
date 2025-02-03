from rest_framework import viewsets
from rest_framework.response import Response
from .models import Users
from .serializers import UsersSerializer


class UsersViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Users.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            instance = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(status=404)
        serializer = UsersSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(status=404)
        serializer = UsersSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            instance = Users.objects.get(pk=pk)
            instance.delete()
            return Response(status=204)
        except Users.DoesNotExist:
            return Response(status=404)
