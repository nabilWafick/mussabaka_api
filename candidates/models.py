from django.db import models
import uuid
from users.models import Users
from schools.models import Schools
from locations.models import Locations
from contests.models import Contests

class Candidates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    locality = models.ForeignKey(Locations, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contests, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
