from django.urls import path
from .views import item_list, add_item

from . import views

app_name = 'inventory'

urlpatterns = [
    # path('items/', item_list, name='item-list'),
    # path('items/add/', add_item, name='add-item'),
    # path('items/<int:tenant_id>/', item_list, name='item-list'),
    # path('items/<int:tenant_id>/add/', add_item, name='add-item'),
    path('tenant/<int:tenant_id>/items/', item_list, name='item-list'),  # For viewing items
    path('tenant/<int:tenant_id>/items/add/', add_item, name='add-item'),  # For adding new item

    # path('purchases/', add_item, name='add-item')
]