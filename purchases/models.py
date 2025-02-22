from django.db import models
from django.contrib.auth.models import User

class WarehouseItem(models.Model):
    ITEM_TYPES = (
        ('laptop', 'Laptop'),
        ('monitor', 'Monitor'),
        ('phone', 'Phone'),
        ('accessory', 'Accessory'),
    )
    
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES)
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    date_added = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.serial_number})"

class LaptopPurchase(models.Model):
    laptop = models.ForeignKey(WarehouseItem, on_delete=models.CASCADE, limit_choices_to={'item_type': 'laptop'})
    date_of_purchase = models.DateField()
    warranty_period = models.IntegerField(help_text="In months")
    sold_to_name = models.CharField(max_length=100)
    sold_to_number = models.CharField(max_length=20)
    sold_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None:  # New purchase
            self.laptop.is_available = False
            self.laptop.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.laptop.name} sold to {self.sold_to_name}"