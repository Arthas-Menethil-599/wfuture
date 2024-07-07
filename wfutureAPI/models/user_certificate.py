from django.db import models

from .volunteer import Volunteer
from .volunteership import Volunteership

class UserCertificate(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    volunteership = models.ForeignKey(Volunteership, on_delete=models.CASCADE)
    date_of_completion = models.DateField()

    def __str__(self):
        return f"{self.volunteer.name} - {self.volunteership.title}"