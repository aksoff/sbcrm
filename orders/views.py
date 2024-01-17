from django.shortcuts import render
from .models import Order
from django.views import generic
from directory.models import Firm
from rest_framework import viewsets
from .serializers import OrderSerializer

def index(request):
    num_orders = Order.objects.all().count()

    return render(request, 'index.html', context = {'num_orders': num_orders})

class OrderListView(generic.ListView):
    model = Order

    def get_context_data(self, **kwargs):
        firm = Firm.objects.first()
        # В первую очередь получаем базовую реализацию контекста
        context = super(OrderListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['some_data'] = firm
        return context


class OrderDetailView(generic.DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        # Получаем реквизиты организации
        firm = Firm.objects.first()
        # В первую очередь получаем базовую реализацию контекста

        context = super(OrderDetailView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['firm'] = firm
        return context


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

