from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.cache import cache

from .models import Products, Category
from financial.forms import UserNewOrderForm
from get_users_ip import get_client_ip


class ProductsList(ListView):
    model = Products
    template_name = 'content/products_list.html'
    context_object_name = 'products'
    paginate_by = 10
    queryset = Products.objects.get_active_product()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data()
        context['categories'] = Category.objects.select_related('parent')

        return context


class DetailProduct(DetailView):
    model = Products
    template_name = 'content/product_detail.html'
    context_object_name = 'products_detail'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(DetailProduct, self).get_context_data()
        context['order_form'] = UserNewOrderForm(self.request.POST or None, initial={'product_id': self.kwargs['pk']})
        return context

    def get(self, request, *args, **kwargs):
        ip = get_client_ip(request)
        pk = kwargs['pk']
        if not cache.get(f'visited_ip:{pk}'):
            cache.set(f'visited_ip:{pk}', [])
            cache.set(f'visit_counter:{pk}', 0)
        visited_ip: list = cache.get(f'visited_ip:{pk}')
        if ip not in visited_ip:
            visited_ip.append(ip)
            visit_counter = cache.get(f'visit_counter:{pk}') + 1
            cache.set(f'visit_counter:{pk}', visit_counter)
            cache.set(f'visited_ip:{pk}', visited_ip)

        return super().get(request, *args, **kwargs)


class ProductSearch(ListView):
    model = Products
    template_name = 'content/products_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        return Products.objects.search(query)
