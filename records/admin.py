from django.contrib import admin
from .models import Laptop, Service, Tenant

# Register your models here
admin.site.register(Laptop)
admin.site.register(Service)
admin.site.register(Tenant)