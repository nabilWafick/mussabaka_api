from rest_framework import serializers
from .models import Schools

class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'
