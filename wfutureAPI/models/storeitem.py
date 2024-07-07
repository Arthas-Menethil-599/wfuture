from django.db import models
from django.urls import reverse

class StoreItem(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to='wfutureAPI\\static\\img\\pictures')
    promocode = models.CharField(max_length=50, null=True, blank=True)
    available = models.BooleanField(default=True)
    points_cost = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"StoreItem {self.pk}"
    
    def get_absolute_url(self):
        return reverse('wfutureAPI:storeitem_detail', args=[self.id])
    