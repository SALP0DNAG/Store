from django.shortcuts import render, HttpResponseRedirect
from .models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request, basket_id):
    if Basket.objects.get(id=basket_id).quantity == 1:
        basket = Basket.objects.get(id=basket_id)
        basket.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = Basket.objects.get(id=basket_id)
        basket.quantity -= 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

