from django.db import models

from .company import Company

from .cause import Cause

from .skill import Skill
from .location import Location

class Volunteership(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    picture = models.ImageField(null=True, blank=True, upload_to='wfutureAPI\\static\\img\\pictures')
    description = models.TextField(null=True, blank=True)
    mission_statement = models.TextField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, through='SkillVolunteerships', blank=True)
    causes = models.ManyToManyField(Cause, through='CauseVolunteerships', blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"Volunteership {self.pk}"
