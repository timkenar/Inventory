from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Laptop, Service
from .serializers import LaptopSerializer, ServiceSerializer
from .utils import call_deepseek_api

from django.shortcuts import render, redirect
from .models import Laptop
# from .forms import LaptopForm  # Create a form if needed


class LaptopViewSet(viewsets.ModelViewSet):
    serializer_class = LaptopSerializer

    def get_queryset(self):
        tenant_id = self.request.headers.get('X-Tenant-ID')
        return Laptop.objects.filter(tenant_id=tenant_id)

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        tenant_id = self.request.headers.get('X-Tenant-ID')
        return Service.objects.filter(laptop__tenant_id=tenant_id)
    
def laptop_list(request):
    tenant_id = request.headers.get('X-Tenant-ID')
    laptops = Laptop.objects.filter(tenant_id=tenant_id)
    return render(request, 'laptops/list.html', {'laptops': laptops})

# def laptop_list(request):
#     tenant_id = request.headers.get('X-Tenant-ID')
#     laptops = Laptop.objects.filter(tenant_id=tenant_id)
    
#     if request.headers.get('HX-Request'):
#         return render(request, 'laptops/partials/laptop_list.html', {'laptops': laptops})
    
#     return render(request, 'laptops/list.html', {'laptops': laptops})


def predict_warranty_expiration(laptop):
    prompt = (
        f"The laptop with serial number {laptop.serial_number} has a warranty end date of {laptop.warranty_end_date}. "
        f"Based on the current date, predict if the warranty is about to expire and provide a recommendation."
    )
    return call_deepseek_api(prompt)

def add_laptop(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number')
        model = request.POST.get('model')
        warranty_start_date = request.POST.get('warranty_start_date')
        warranty_end_date = request.POST.get('warranty_end_date')
        tenant_id = request.headers.get('X-Tenant-ID')

        laptop = Laptop.objects.create(
            tenant_id=tenant_id,
            serial_number=serial_number,
            model=model,
            warranty_start_date=warranty_start_date,
            warranty_end_date=warranty_end_date,
        )
        return render(request, 'laptops/laptop_item.html', {'laptop': laptop})
    return render(request, 'laptops/add_laptop.html')

def add_service(request, laptop_id):
    if request.method == 'POST':
        service_date = request.POST.get('service_date')
        description = request.POST.get('description')
        cost = request.POST.get('cost')

        service = Service.objects.create(
            laptop_id=laptop_id,
            service_date=service_date,
            description=description,
            cost=cost,
        )
        return render(request, 'laptops/service_item.html', {'service': service})
    return render(request, 'laptops/add_service.html', {'laptop_id': laptop_id})

@api_view(['GET'])
def predict_warranty(request, laptop_id):
    laptop = Laptop.objects.get(id=laptop_id)
    prediction = predict_warranty_expiration(laptop)
    return Response({"prediction": prediction})

@api_view(['GET'])
def suggest_services(request, laptop_id):
    laptop = Laptop.objects.get(id=laptop_id)
    suggestions = suggest_services(laptop)
    return Response({"suggestions": suggestions})