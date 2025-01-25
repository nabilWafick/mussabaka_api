from rest_framework import viewsets
from .models import Schools
from .serializers import SchoolsSerializer

class SchoolsViewSet(viewsets.ModelViewSet):
    queryset = Schools.objects.all().order_by('name')
    serializer_class = SchoolsSerializer
