from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('records.urls')),
    path('inventory/', include('inventory.urls')),
    path('core/', include('core.urls')),
    # path('sales/',include('sales.urls'))
]
