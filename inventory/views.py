from django.shortcuts import render, get_object_or_404
from .models import Item
from core.models import Tenant

def item_list(request, tenant_id):
    tenant = get_object_or_404(Tenant, id=tenant_id)
    items = Item.objects.filter(tenant=tenant)
    context = {
        'tenant': tenant,
        'items': items,
    }
    return render(request, 'inventory/item_list.html', context)

def add_item(request, tenant_id):
    if request.method == 'POST':
        # Fetching data from POST request
        name = request.POST.get('name')
        serial_number = request.POST.get('serial_number')
        quantity = request.POST.get('quantity')
        expiration_date = request.POST.get('expiration_date')

        tenant = get_object_or_404(Tenant, id=tenant_id)
        item = Item.objects.create(
            tenant=tenant,
            name=name,
            serial_number=serial_number,
            quantity=quantity,
            expiration_date=expiration_date,
        )
        return render(request, 'inventory/item_item.html', {'item': item})

    return render(request, 'inventory/add_item.html', {'tenant_id': tenant_id})


# from django.shortcuts import render
# from .models import Item

# from django.shortcuts import render, get_object_or_404
# from core.models import Tenant

# def item_list(request, tenant_id):
#     tenant = get_object_or_404(Tenant, id=tenant_id)
#     items = Item.objects.filter(tenant=tenant)
#     context = {
#         'tenant': tenant,
#         'items': items,
#     }
#     return render(request, 'inventory/item_list.html', context)


# def add_item(request):
#     if request.method == 'POST':
#         tenant_id = request.headers.get('X-Tenant-ID')
#         name = request.POST.get('name')
#         serial_number = request.POST.get('serial_number')
#         quantity = request.POST.get('quantity')
#         expiration_date = request.POST.get('expiration_date')

#         item = Item.objects.create(
#             tenant_id=tenant_id,
#             name=name,
#             serial_number=serial_number,
#             quantity=quantity,
#             expiration_date=expiration_date,
#         )
#         return render(request, 'inventory/item_item.html', {'item': item})
#     return render(request, 'inventory/add_item.html')