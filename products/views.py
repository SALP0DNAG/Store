from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)


def profile(request):
    return render(request, 'products/profile.html')
