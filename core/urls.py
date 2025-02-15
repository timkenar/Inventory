from django.urls import path
from .views import dashboard

urlpatterns = [
    path('dashboard/<int:tenant_id>/', dashboard, name='dashboard'),
]