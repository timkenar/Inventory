from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Item, Sale, Order, Report
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F

def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')  # Redirect to dashboard without tenant_id
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('core:dashboard')  # Redirect to dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('core:login')

@login_required
def dashboard(request):
    total_items = Item.objects.count()
    total_sales = Sale.objects.aggregate(total=Sum('amount'))['total'] or 0
    pending_orders = Order.objects.filter(status='pending').count()
    low_stock_count = Item.objects.filter(quantity__lt=F('low_stock_threshold')).count()
    recent_activities = Order.objects.order_by('-created_at')[:5]  # Placeholder
    system_alerts = [
        {'title': 'Low Stock Alert', 'message': 'Check inventory for low stock items', 'severity_class': 'bg-yellow-100'},
        {'title': 'System Update', 'message': 'New features available', 'severity_class': 'bg-blue-100'},
    ]

    context = {
        'total_items': total_items,
        'total_sales': total_sales,
        'pending_orders': pending_orders,
        'low_stock_count': low_stock_count,
        'recent_activities': recent_activities,
        'system_alerts': system_alerts,
        'user': request.user,
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def inventory(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'core/inventory.html', context)

@login_required
def sales(request):
    sales = Sale.objects.order_by('-date')
    context = {'sales': sales}
    return render(request, 'core/sales.html', context)

@login_required
def purchases(request):
    orders = Order.objects.order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'core/purchases.html', context)

@login_required
def reports(request):
    reports = Report.objects.order_by('-generated_at')
    context = {'reports': reports}
    return render(request, 'core/reports.html', context)


@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'core/profile.html', context)
# # core/views.py
# from django.shortcuts import render,redirect
# # , get_object_or_404
# from django.contrib.auth import authenticate, login, logout
# from core.models import Tenant
# from django.contrib import messages
# from django.shortcuts import render
# from .models import Tenant, Item, Sale, Order, Report
# from django.contrib.auth.decorators import login_required

# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('core:dashboard', tenant_id=1)  # Adjust tenant_id as needed
        
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             # Get the tenant associated with the user (adjust based on your model structure)
#             tenant_id = getattr(user, 'tenant_id', 1)  # Default to 1 if not set
#             return redirect('core:dashboard', tenant_id=tenant_id)
#         else:
#             messages.error(request, 'Invalid username or password.')
    
#     return render(request, 'core/login.html')

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have been successfully logged out.')
#     return redirect('core:login')



# @login_required
# def dashboard(request):
#     tenant = Tenant.objects.get(id=request.user.tenant_id)  # Assume tenant is linked to user
#     total_items = Item.objects.filter(tenant=tenant).count()
#     total_sales = Sale.objects.filter(tenant=tenant).aggregate(total=Sum('amount'))['total'] or 0
#     pending_orders = Order.objects.filter(tenant=tenant, status='pending').count()
#     low_stock_count = Item.objects.filter(tenant=tenant, quantity__lt=F('low_stock_threshold')).count()
#     recent_activities = Order.objects.filter(tenant=tenant).order_by('-created_at')[:5]  # Placeholder
#     system_alerts = [
#         {'title': 'Low Stock Alert', 'message': 'Check inventory for low stock items', 'severity_class': 'bg-yellow-100'},
#         {'title': 'System Update', 'message': 'New features available', 'severity_class': 'bg-blue-100'},
#     ]

#     context = {
#         'tenant': tenant,
#         'total_items': total_items,
#         'total_sales': total_sales,
#         'pending_orders': pending_orders,
#         'low_stock_count': low_stock_count,
#         'recent_activities': recent_activities,
#         'system_alerts': system_alerts,
#         'user': request.user,
#     }
#     return render(request, 'core/dashboard.html', context)

# @login_required
# def inventory(request):
#     tenant = Tenant.objects.get(id=request.user.tenant_id)
#     items = Item.objects.filter(tenant=tenant)
#     context = {'tenant': tenant, 'items': items}
#     return render(request, 'core/inventory.html', context)

# @login_required
# def sales(request):
#     tenant = Tenant.objects.get(id=request.user.tenant_id)
#     sales = Sale.objects.filter(tenant=tenant).order_by('-date')
#     context = {'tenant': tenant, 'sales': sales}
#     return render(request, 'core/sales.html', context)

# @login_required
# def purchases(request, tenant_id):
#     tenant = Tenant.objects.get(id=tenant_id)
#     orders = Order.objects.filter(tenant=tenant).order_by('-created_at')
#     context = {'tenant': tenant, 'orders': orders}
#     return render(request, 'core/purchases.html', context)

# @login_required
# def reports(request):
#     tenant = Tenant.objects.get(id=request.user.tenant_id)
#     reports = Report.objects.filter(tenant=tenant).order_by('-generated_at')
#     context = {'tenant': tenant, 'reports': reports}
#     return render(request, 'core/reports.html', context)