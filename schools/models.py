from django.db import models
import uuid
from locations.models import Locations

class Schools(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    locality = models.ForeignKey(Locations, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meta:
        verbose_name_plural = "Schools"