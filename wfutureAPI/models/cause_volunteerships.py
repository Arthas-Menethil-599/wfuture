from django.db import models
from .cause import Cause
from .volunteership import Volunteership

class CauseVolunteerships(models.Model):
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
    volunteership = models.ForeignKey(Volunteership, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"CauseVolunteership {self.pk}"