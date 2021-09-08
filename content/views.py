from django.shortcuts import render
from django.views.generic import ListView

from .models import Products


class ProductsList(ListView):
    model = Products
    template_name = 'content/products_list.html'
    context_object_name = 'products'