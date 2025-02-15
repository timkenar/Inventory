from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='tenant_logos/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, default='#000000')  # Hex color code
    secondary_color = models.CharField(max_length=7, default='#FFFFFF')  # Hex color code
    motto = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name