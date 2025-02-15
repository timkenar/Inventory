from django.shortcuts import render, get_object_or_404
from core.models import Tenant
from inventory.models import Item
# from sales.models import Sale

def dashboard(request, tenant_id):
    tenant = get_object_or_404(Tenant, id=tenant_id)
    total_items = Item.objects.filter(tenant=tenant).count()
    # total_sales = Sale.objects.filter(tenant=tenant).aggregate(total_sales=models.Sum('amount'))['total_sales'] or 0
    # pending_orders = Sale.objects.filter(tenant=tenant, status='pending').count()

    context = {
        'tenant': tenant,
        'total_items': total_items,
        # 'total_sales': total_sales,
        # 'pending_orders': pending_orders,
    }
    return render(request, 'core/dashboard.html', context)

# from django.shortcuts import render, get_object_or_404
# from .models import Tenant
# from inventory.models import Item
# from sales.models import Sale  # Assuming you have a Sale model

# def dashboard(request, tenant_id):
#     tenant = get_object_or_404(Tenant, id=tenant_id)
#     total_items = Item.objects.filter(tenant=tenant).count()
#     total_sales = Sale.objects.filter(tenant=tenant).aggregate(total_sales=models.Sum('amount'))['total_sales'] or 0
#     pending_orders = Sale.objects.filter(tenant=tenant, status='pending').count()

#     context = {
#         'tenant': tenant,
#         'total_items': total_items,
#         'total_sales': total_sales,
#         'pending_orders': pending_orders,
#     }
#     return render(request, 'core/dashboard.html', context)