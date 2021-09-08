from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Products


class ProductsList(ListView):
    model = Products
    template_name = 'content/products_list.html'
    context_object_name = 'products'


class DetailProduct(DetailView):
    model = Products
    template_name = 'content/product_detail.html'
    context_object_name = 'products_detail'
    pk_url_kwarg = 'pk'
