from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import WarehouseItem, LaptopPurchase
from .forms import WarehouseItemForm, LaptopPurchaseForm
from django.contrib import messages

@login_required
def warehouse(request):
    if request.method == 'POST':
        form = WarehouseItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added to warehouse successfully!')
            return redirect('purchases:warehouse')
    else:
        form = WarehouseItemForm()
    
    items = WarehouseItem.objects.all()
    return render(request, 'purchases/warehouse.html', {'form': form, 'items': items})

@login_required
def purchase_sheet(request):
    purchases = LaptopPurchase.objects.all()
    return render(request, 'purchases/purchase_sheet.html', {'purchases': purchases})

@login_required
def laptops(request):
    if request.method == 'POST':
        form = LaptopPurchaseForm(request.POST)
        if form.is_valid():
            serial_number = form.cleaned_data['laptop'].serial_number
            if WarehouseItem.objects.filter(serial_number=serial_number, is_available=True).exists():
                purchase = form.save(commit=False)
                purchase.sold_by = request.user
                purchase.save()
                messages.success(request, 'Laptop purchase recorded successfully!')
                return redirect('purchases:laptops')
            else:
                messages.error(request, 'Laptop is not available in warehouse!')
    else:
        form = LaptopPurchaseForm()
    
    laptops = LaptopPurchase.objects.all()
    return render(request, 'purchases/laptops.html', {'form': form, 'laptops': laptops})

@login_required
def check_availability(request):
    serial_number = request.GET.get('serial_number', '')
    item = WarehouseItem.objects.filter(serial_number=serial_number, item_type='laptop').first()
    if item:
        return JsonResponse({'available': item.is_available})
    return JsonResponse({'available': False, 'error': 'Laptop not found'})