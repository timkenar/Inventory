from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Item, Sale, Order, Report
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User




def landing_page(request):
    return render(request, 'landing.html', {'user': request.user})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


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

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required
def profile_edit(request):
    return render(request, 'core/profile_edit.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        
        try:
            user.save()
            update_session_auth_hash(request, user)  # Important for keeping user logged in
            messages.success(request, 'Profile updated successfully!')
            return render(request, 'core/profile_edit.html')
        except Exception as e:
            messages.error(request, f'Error updating profile: {str(e)}')
            return render(request, 'core/profile_edit.html')
    
    return HttpResponse(status=405)



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



# views.py
from django.shortcuts import render

def toggle_sidebar(request):
    # This could be stored in session or user preferences in a real app
    is_collapsed = request.session.get('sidebar_collapsed', False)
    request.session['sidebar_collapsed'] = not is_collapsed
    
    context = {
        'is_collapsed': not is_collapsed,
        'user': request.user,
    }
    return render(request, 'core/sidebar.html', context)

@login_required
def settings(request):
    return render(request, 'core/settings.html')

