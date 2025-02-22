from django import forms
from .models import WarehouseItem, LaptopPurchase

class WarehouseItemForm(forms.ModelForm):
    class Meta:
        model = WarehouseItem
        fields = ['item_type', 'name', 'serial_number']
        widgets = {
            'item_type': forms.Select(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300'}),
            'name': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300'}),
            'serial_number': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300'}),
        }

class LaptopPurchaseForm(forms.ModelForm):
    class Meta:
        model = LaptopPurchase
        fields = ['laptop', 'date_of_purchase', 'warranty_period', 'sold_to_name', 'sold_to_number']
        widgets = {
            'laptop': forms.Select(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300', 'hx-get': '/purchases/check-availability/', 'hx-trigger': 'change', 'hx-target': '#availability-status'}),
            'date_of_purchase': forms.DateInput(attrs={'type': 'date', 'class': 'mt-1 block w-full rounded-md border-gray-300'}),
            'warranty_period': forms.NumberInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300'}),
            'sold_to_name': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300'}),
            'sold_to_number': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300'}),
        }