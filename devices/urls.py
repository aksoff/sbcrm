from django.urls import include, path
from . import views


urlpatterns = [
    #path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

