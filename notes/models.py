from django.db import models
import uuid

from jury.models import Jury
from questionnaires.models import Questionnaires

class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    questionnaire = models.ForeignKey(Questionnaires, on_delete=models.CASCADE)
    jury = models.ForeignKey(Jury, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
