from django.db import models
from django.contrib.auth.models import User

from .skill import Skill

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    avatar = models.ImageField(null=True, blank=True, upload_to='wfutureAPI\\static\\img\\avatars')
    sex = models.CharField(max_length=50, choices=[('male', 'Male'), ('female', 'Female'), ('prefer_not_to_say', 'Prefer not to say')], null=True, blank=True)
    birthday= models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    points = models.IntegerField(default=0)
    skills = models.ManyToManyField(Skill, through='SkillVolunteer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"Volunteer {self.pk}"
