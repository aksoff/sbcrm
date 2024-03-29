"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from devices.views import BrandViewSet, DeviceViewSet
from orders.views import OrderViewSet

admin.site.site_header = 'SERVBIT.CRM'

router = SimpleRouter()
router.register('api/v1/brands', BrandViewSet)
router.register('api/v1/devices', DeviceViewSet)
#router.register('api/v1/orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('orders.urls')),
]

urlpatterns += router.urls

urlpatterns += [
    path('directory/', include('directory.urls')),
    path('devices/', include('devices.urls')),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
