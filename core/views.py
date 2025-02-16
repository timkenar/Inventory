# core/views.py
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Tenant
from inventory.models import Item
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard', tenant_id=1)  # Adjust tenant_id as needed
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Get the tenant associated with the user (adjust based on your model structure)
            tenant_id = getattr(user, 'tenant_id', 1)  # Default to 1 if not set
            return redirect('core:dashboard', tenant_id=tenant_id)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('core:login')

# Update your existing dashboard view to require login
@login_required(login_url='core:login')
def dashboard(request, tenant_id):
    # Your existing dashboard code here
    pass



@login_required
def dashboard(request, tenant_id):
    tenant = get_object_or_404(Tenant, id=tenant_id)
    
    # Basic stats
    total_items = Item.objects.filter(tenant=tenant).count()
    
    context = {
        'tenant': tenant,
        'total_items': total_items,
        'total_sales': 0,  # Placeholder
        'pending_orders': 0,  # Placeholder
    }
    
    return render(request, 'core/dashboard.html', context)

# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.db.models import F 
# from core.models import Tenant
# from inventory.models import Item
# from datetime import datetime, timedelta
# from django.db.models import Count, Sum

# @login_required
# def dashboard(request, tenant_id):
#     tenant = get_object_or_404(Tenant, id=tenant_id)
    
#     # Basic stats
#     total_items = Item.objects.filter(tenant=tenant).count()
#     low_stock_count = Item.objects.filter(tenant=tenant, quantity__lte=F('minimum_stock_level')).count()
    
#     # Recent activities (last 7 days)
#     recent_activities = []
    
#     # Example activity types and their colors
#     activity_colors = {
#         'create': 'bg-green-500',
#         'update': 'bg-blue-500',
#         'delete': 'bg-red-500',
#     }
    
#     # System alerts
#     system_alerts = []
    
#     # Check for low stock items
#     low_stock_items = Item.objects.filter(tenant=tenant, quantity__lte=F('minimum_stock_level'))
#     if low_stock_items.exists():
#         system_alerts.append({
#             'severity_class': 'bg-yellow-100 text-yellow-800',
#             'title': 'Low Stock Alert',
#             'message': f'{low_stock_items.count()} items are running low on stock.'
#         })
    
#     # Check for expired items
#     expired_items = Item.objects.filter(tenant=tenant, expiration_date__lte=datetime.now().date())
#     if expired_items.exists():
#         system_alerts.append({
#             'severity_class': 'bg-red-100 text-red-800',
#             'title': 'Expired Items',
#             'message': f'{expired_items.count()} items have expired.'
#         })

#     context = {
#         'tenant': tenant,
#         'total_items': total_items,
#         'low_stock_count': low_stock_count,
#         'recent_activities': recent_activities,
#         'system_alerts': system_alerts,
#         'unread_notifications_count': request.user.notifications.unread().count(),
#     }
    
#     return render(request, 'core/dashboard.html', context)

# @login_required
# def notifications(request):
#     notifications = request.user.notifications.all()[:5]
#     return render(request, 'core/notifications_dropdown.html', {'notifications': notifications})






# from django.shortcuts import render, get_object_or_404
# from core.models import Tenant
# from inventory.models import Item
# # from sales.models import Sale

# def dashboard(request, tenant_id):
#     tenant = get_object_or_404(Tenant, id=tenant_id)
#     total_items = Item.objects.filter(tenant=tenant).count()
#     # total_sales = Sale.objects.filter(tenant=tenant).aggregate(total_sales=models.Sum('amount'))['total_sales'] or 0
#     # pending_orders = Sale.objects.filter(tenant=tenant, status='pending').count()

#     context = {
#         'tenant': tenant,
#         'total_items': total_items,
#         # 'total_sales': total_sales,
#         # 'pending_orders': pending_orders,
#     }
#     return render(request, 'core/dashboard.html', context)
