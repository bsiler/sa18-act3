from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Product

def product_index(request): 
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def product_show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/show.html', {'product': product})