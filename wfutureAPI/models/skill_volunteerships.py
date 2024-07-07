from django.db import models
from .skill import Skill
from .volunteership import Volunteership

class SkillVolunteerships(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    volunteership = models.ForeignKey(Volunteership, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"SkillVolunteership {self.pk}"
