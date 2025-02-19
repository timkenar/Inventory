from django.db import models
from django.contrib.auth.models import User

class Tenant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='tenant_logos/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, default='#000000')  # Hex color code
    secondary_color = models.CharField(max_length=7, default='#FFFFFF')  # Hex color code
    motto = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Sale(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.item.name} - ${self.amount}"

class Order(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default='pending')  # e.g., 'pending', 'completed'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.item.name} - {self.status}"

class Report(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# from django.db import models

# class Tenant(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     logo = models.ImageField(upload_to='tenant_logos/', blank=True, null=True)
#     primary_color = models.CharField(max_length=7, default='#000000')  # Hex color code
#     secondary_color = models.CharField(max_length=7, default='#FFFFFF')  # Hex color code
#     motto = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name