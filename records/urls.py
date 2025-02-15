from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LaptopViewSet, ServiceViewSet, laptop_list,predict_warranty, suggest_services, add_laptop, add_service

# router = DefaultRouter()
# router.register(r'laptops', LaptopViewSet, basename='laptop')
# router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    # path('', include(router.urls)),
    path('laptops/view/', laptop_list, name='laptop-list'),
    path('laptops/<int:laptop_id>/predict_warranty/', predict_warranty, name='predict-warranty'),
    path('laptops/<int:laptop_id>/suggest_services/', suggest_services, name='suggest-services'),
    path('laptops/add/', add_laptop, name='add-laptop'),
    path('laptops/<int:laptop_id>/add_service/', add_service, name='add-service'),
]