from django.db import models
import uuid
from locations.models import Locations
from users.models import Users

class Contests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Meta:
        verbose_name_plural = "Contests"
