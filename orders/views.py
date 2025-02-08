from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer


class Orders(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def form(request):
    if request.method == 'POST':
        product_type = request.POST.get('product_type')
        size = request.POST.get('size')
        requester_name = request.POST.get('requester_name')
        quantity = request.POST.get('quantity')
        manufacturer = request.POST.get('manufacturer')
        unloading_place = request.POST.get('unloading_place')
        description = request.POST.get('description')

        if product_type and size and requester_name and quantity and manufacturer and unloading_place:
            Order.objects.create(
                product_type=product_type,
                size=size,
                requester_name=requester_name,
                quantity=int(quantity),
                manufacturer=manufacturer,
                unloading_place=unloading_place,
                description=description
            )
            return redirect('order_form')

    return render(request, 'order_form.html')