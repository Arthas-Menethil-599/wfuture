from django.db import models
from django.contrib.auth.models import User
from .storeitem import StoreItem

class Transaction(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    storeitem = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_points = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} by {self.volunteer.username}"
