
from django.urls import path
from product.views import info_order, info_product
app_name = 'product'

urlpatterns = [
    path('', info_product, name='product'),
    path('orders/', info_order, name='orders'),
]
