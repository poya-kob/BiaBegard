from django.shortcuts import render
from django.views.generic import ListView

from .models import Products, Category


class ProductsList(ListView):
    model = Products
    template_name = 'content/products_list.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
