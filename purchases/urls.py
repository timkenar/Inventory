from django.urls import path
from . import views

app_name = 'purchases'


urlpatterns = [
    path('warehouse/', views.warehouse, name='warehouse'),
    path('purchase-sheet/', views.purchase_sheet, name='purchase_sheet'),
    path('laptops/', views.laptops, name='laptops'),
    path('check-availability/', views.check_availability, name='check_availability'),
]