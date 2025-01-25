from rest_framework import viewsets
from .models import Surahs
from .serializers import SurahsSerializer

class SurahsViewSet(viewsets.ModelViewSet):
    queryset = Surahs.objects.all().order_by('name')
    serializer_class = SurahsSerializer
