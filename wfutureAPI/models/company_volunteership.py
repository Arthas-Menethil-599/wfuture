from django.db import models
from .company import Company
from .volunteership import Volunteership

class CompanyVolunteership(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    volunteership = models.ForeignKey(Volunteership, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} - {self.volunteership}"