from django.urls import path
from .views import login_view, logout_view
from . import views

app_name = 'core'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('sales/', views.sales, name='sales'),
    path('purchases/<int:tenant_id>/', views.purchases, name='purchases'),
    path('reports/', views.reports, name='reports'),
]
