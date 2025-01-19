from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer


class Orders(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def form(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        product_name = request.POST['product']
        quantity = request.POST['quantity']
        Order.objects.create(
            customer_name=customer_name,
            product_name=product_name,
            quantity=quantity
        )
        return render(request, 'order_form.html', {'success': 'سفارش شما ثبت شد!'})
    return render(request, 'order_form.html')


