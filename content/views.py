from django.shortcuts import render
from django.views.generic import ListView

from .models import Products


class ProductsList(ListView):
    model = Products
    template_name = 'content/products_list.html'
    context_object_name = 'products'


def products_list(request):
    context = {
        'products': Products.objects.get_active_product()
    }
    return render(request, 'content/products_list.html', context)
