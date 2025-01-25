from django.db import models
import uuid

from surahs.models import Surahs
from categories.models import Categories
from candidates.models import Candidates
from contests.models import Contests

class Questionnaires(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    candidate = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contests, on_delete=models.CASCADE)
    surah = models.ForeignKey(Surahs, on_delete=models.CASCADE)
    start_verse = models.IntegerField()
    end_verse = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
