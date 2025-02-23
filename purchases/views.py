from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import WarehouseItem, LaptopPurchase
from .forms import WarehouseItemForm, LaptopPurchaseForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

@login_required
def warehouse(request):
    if request.method == 'POST':
        form = WarehouseItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added to warehouse successfully!')
            return redirect('purchases:warehouse')
        else:
            messages.error(request, 'Failed to add item. Please check the form.')
    else:
        form = WarehouseItemForm()

    # Get queryset
    items = WarehouseItem.objects.all()

    # Apply filters
    search_query = request.GET.get('q', '')
    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) |
            Q(serial_number__icontains=search_query)
        )

    item_type = request.GET.get('type', '')
    if item_type:
        items = items.filter(item_type=item_type)

    available = request.GET.get('available', '')
    if available in ('true', 'false'):
        items = items.filter(is_available=(available == 'true'))

    # Order the results (you can modify this as needed)
    items = items.order_by('name')

    # Pagination
    paginator = Paginator(items, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass item type choices for the filter dropdown
    item_types = WarehouseItem.ITEM_TYPE_CHOICES if hasattr(WarehouseItem, 'ITEM_TYPE_CHOICES') else []

    return render(request, 'purchases/warehouse.html', {
        'form': form,
        'page_obj': page_obj,
        'item_types': item_types,
        'total_items': paginator.count,
    })

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