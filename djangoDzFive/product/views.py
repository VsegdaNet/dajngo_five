from django.shortcuts import render
from product.models import Order, Product



def info_order(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }

    return render(request, 'product/info_order.html', context=context)

def info_product(request):
    product = Product.objects.all()
    context = {
        'product': product
    }

    return render(request, 'product/info_product.html', context=context)