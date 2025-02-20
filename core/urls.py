from django.urls import path
from . import views
from django.urls import path, include
from . import views



app_name = 'core'

urlpatterns = [
    
    # # React Urls
    # path('', include(router.urls)),
   


    # HTMX Urls
    path('', views.landing_page, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('sales/', views.sales, name='sales'),
    path('purchases/', views.purchases, name='purchases'),  # Removed tenant_id
    path('reports/', views.reports, name='reports'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]