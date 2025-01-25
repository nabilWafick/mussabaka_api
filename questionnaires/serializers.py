from rest_framework import serializers
from .models import Questionnaires

class QuestionnairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaires
        fields = '__all__'
