from django.db import models
from .volunteer import Volunteer
from .volunteership import Volunteership

class Application(models.Model):
    application_content = models.TextField(null=True, blank=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    volunteership = models.ForeignKey(Volunteership, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="unchecked", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"Application {self.pk}"