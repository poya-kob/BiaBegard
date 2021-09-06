from django.shortcuts import render
from .models import Products


def products_list(request):
    context = {}
    return render(request, 'comments/list_of_products.html', context)


def list_products(request):
    list_products_qs = Products.objects.defer('name', 'image', 'product_price', 'off_price')
    context = {
        'list_products': list_products_qs,
        'title': ' لیست محصولات ',
    }

    return render(request, '', context)


def detail_product(request, pid):
    detail_product_qs = Products.objects.get(id=pid)

    context = {
        'detail_product': detail_product_qs,
        'title': 'جزئیات محصول'
    }

    return render(request, '', context)
