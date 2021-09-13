from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Products, Category
from django.db.models import Avg


class ProductsList(ListView):
    model = Products
    template_name = 'content/products_list.html'
    context_object_name = 'products'
    paginate_by = 6
    queryset = Products.objects.get_active_product()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data()
        # context['categories'] = Category.objects.all()

        context['price_ave'] = Products.objects.aggregate(price_average=Avg('product_price'))["price_average"]
        print(context)
        return context


class DetailProduct(DetailView):
    model = Products
    template_name = 'content/product_detail.html'
    context_object_name = 'products_detail'
    pk_url_kwarg = 'pk'

    # def get_context_data(self, **kwargs):
    #     context = super(DetailProduct, self).get_context_data()
    #     context['related_products']=Products.objects.filter(category=)


class ProductSearch(ListView):
    model = Products
    template_name = 'content/products_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        return Products.objects.search(query)
