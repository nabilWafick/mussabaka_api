from rest_framework import serializers
from .models import Surahs

class SurahsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surahs
        fields = '__all__'
