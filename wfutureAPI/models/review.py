from django.db import models
from .company import Company
from .volunteer import Volunteer
from .volunteership import Volunteership

class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    volunteership = models.ForeignKey(Volunteership, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"Review from {self.volunteership.title} ({self.company.name})"
