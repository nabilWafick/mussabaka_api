from rest_framework import viewsets
from .models import Questionnaires
from .serializers import QuestionnairesSerializer

class QuestionnairesViewSet(viewsets.ModelViewSet):
    queryset = Questionnaires.objects.all().order_by('id')
    serializer_class = QuestionnairesSerializer
