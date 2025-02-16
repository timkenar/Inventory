from django.urls import path
from .views import dashboard

app_name = 'core'

urlpatterns = [
    path('dashboard/<int:tenant_id>/', dashboard, name='dashboard'),
]