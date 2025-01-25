from rest_framework import viewsets
from .models import Contests
from .serializers import ContestsSerializer

class ContestsViewSet(viewsets.ModelViewSet):
    queryset = Contests.objects.all().order_by('name')
    serializer_class = ContestsSerializer
