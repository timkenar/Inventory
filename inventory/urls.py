from django.urls import path
from .views import item_list, add_item


app_name = 'inventory'

urlpatterns = [
    # path('items/', item_list, name='item-list'),
    # path('items/add/', add_item, name='add-item'),
    path('items/<int:tenant_id>/', item_list, name='item-list'),
    path('items/<int:tenant_id>/add/', add_item, name='add-item'),
]