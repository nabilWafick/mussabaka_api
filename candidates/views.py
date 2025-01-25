from rest_framework import viewsets
from .models import Candidates
from .serializers import CandidatesSerializer

class CandidatesViewSet(viewsets.ModelViewSet):
    queryset = Candidates.objects.all().order_by('id')
    serializer_class = CandidatesSerializer
