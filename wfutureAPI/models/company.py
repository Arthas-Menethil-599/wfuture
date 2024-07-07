from django.db import models
from django.contrib.auth.models import User
from .location import Location

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="wfutureAPI\\static\\img\\avatars")
    name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    mission = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


