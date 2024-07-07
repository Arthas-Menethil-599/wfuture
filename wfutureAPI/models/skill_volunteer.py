from django.db import models
from .volunteer import Volunteer
from .skill import Skill

class SkillVolunteer(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"SkillVolunteer {self.pk}"
