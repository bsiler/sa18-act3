from django.shortcuts import render

from .models import Product
def product_index(request): 
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})