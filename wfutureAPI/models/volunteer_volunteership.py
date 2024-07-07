from django.db import models
from .volunteer import Volunteer
from .volunteership import Volunteership

class VolunteerVolunteership(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    volunteership = models.ForeignKey(Volunteership, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="active", null=False, blank=False)
    recieved_points = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"VolunteerVolunteership {self.pk}"