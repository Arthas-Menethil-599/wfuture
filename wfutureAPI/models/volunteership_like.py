from django.db import models
from .volunteer import Volunteer
from .volunteership import Volunteership

class VolunteershipLike(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    volunteership = models.ForeignKey(Volunteership, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"VolunteershipLike {self.pk}"