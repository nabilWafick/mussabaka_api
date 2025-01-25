from rest_framework import viewsets
from .models import Jury
from .serializers import JurySerializer

class JuryViewSet(viewsets.ModelViewSet):
    queryset = Jury.objects.all().order_by('name')
    serializer_class = JurySerializer
