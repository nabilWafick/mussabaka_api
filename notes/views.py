from rest_framework import viewsets
from .models import Notes
from .serializers import NotesSerializer

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all().order_by('id')
    serializer_class = NotesSerializer
