from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Laptop(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='laptops')
    serial_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100)
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model} ({self.serial_number})"

class Service(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='services')
    service_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Service for {self.laptop} on {self.service_date}"