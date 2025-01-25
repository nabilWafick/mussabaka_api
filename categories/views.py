from rest_framework import viewsets
from .models import Categories
from .serializers import CategoriesSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('id')
    serializer_class = CategoriesSerializer
