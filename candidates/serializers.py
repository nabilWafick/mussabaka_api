from rest_framework import serializers
from .models import Candidates

class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields = '__all__'
