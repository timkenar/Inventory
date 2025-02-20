from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # path('api/login/', views.user_login, name='login'),
    # path('api/register/', views.user_register, name='register'),
    # path('api/logout/', views.user_logout, name='logout'),
    # path('api/dashboard/', views.dashboard_data, name='dashboard'),
    # path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    # path('check-auth/', views.check_auth, name='check_auth'),

    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)