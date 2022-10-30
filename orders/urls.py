from django.urls import include, path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^orders/$', views.OrderListView.as_view(), name='orders'),
    url(r'^order/(?P<pk>\d+)$', views.OrderDetailView.as_view(), name='order-detail'),
]