from django.db import models
from core.models import Tenant

class Item(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100, unique=True)
    batch_number = models.CharField(max_length=100, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"
    

class Warehouse(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='warehouses')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.location})"