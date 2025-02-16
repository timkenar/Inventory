from django.urls import path
from .views import dashboard, login_view, logout_view

app_name = 'core'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/<int:tenant_id>/', dashboard, name='dashboard'),
]