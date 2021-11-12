from django.shortcuts import redirect, render, reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import UserNewOrderForm
from .models import Carts, CartItems
from account.models import Suppliers, Customers
from iran_zone.models import Ostan, Shahrestan, Shahr, Dehestan


@login_required()
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        cart = Carts.objects.filter(user_id=request.user.id).first()
        if not cart:
            cart = Carts.objects.create(user_id=request.user.id)
        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count <= 0:
            count = 1
        cart_item = cart.cart_items.filter(product_id=product_id, status="pending").first()
        if cart_item:
            if cart_item.qty + count <= cart_item.product.inventory:
                cart_item.qty += count
                cart_item.save()
            elif cart_item.product.inventory > 1:
                cart_item.qty = cart_item.product.inventory
                cart_item.save()
        else:
            cart.cart_items.create(product_id=product_id, qty=count)

    return redirect('/')


@login_required()
def delete_user_order(request):
    CartItems.objects.get(id=request.GET.get('id')).delete()
    return redirect('/')


@login_required()
def check_out_step1(request):
    cart_items = Carts.objects.filter(user_id=request.user.id).first()
    request.session['red_carpet'] = True
    total_price = 0
    for item in cart_items.cart_items.filter(status='pending'):
        total_price += item.total_price_product
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'financial/check_to_pay.html', context)


@login_required()
def pay_page(request):
    if request.method == "POST":
        address_id = request.POST.get('address')
        request.user_obj.address.all().update(is_selected=False)
        got_add = request.user_obj.address.get(id=int(address_id))
        got_add.is_selected = True
        got_add.save()

    context = {}
    cart = Carts.objects.get(user_id=request.user.id)
    items = cart.cart_items.filter(status='pending', is_selected=True)
    total_price = 0
    for item in items:
        total_price += item.total_price_product
    context['cart_items'] = items
    context['total_price'] = total_price
    return render(request, 'financial/pay_item.html', context)


class SelectAddress(View):
    context = {
        'all_ostan': Ostan.objects.all(),
        'all_shahrestan': Shahrestan.objects.all(),
        'all_shahr': Shahr.objects.all(),
        'all_rosta': Dehestan.objects.all(),
        'user_obj': None
    }

    def get(self, request):
        return render(request, "financial/add_select_address.html", self.context)

    def post(self, request):
        ostan = request.POST.get("ostan")
        shahrestan = request.POST.get("shahrestan")
        zip_code = request.POST.get("zipCode")
        full_address = request.POST.get("fullAddress")
        rosta = None
        shahr = None
        shahr = request.POST.get("shahr", None)
        rosta = request.POST.get("rosta", None)
        request.user_obj.address.create(province_id=ostan, township_id=shahrestan, city_id=shahr, village=rosta,
                                        zip_code=zip_code, full_address=full_address)
        return render(request, "financial/add_select_address.html", self.context)


class GetSelectedCartItems(View):
    def post(self, request):
        if 'red_carpet' not in request.session:
            return redirect(reverse('check_step1'))
        cart = Carts.objects.get(user_id=request.user.id)
        cart_items = []
        del request.session['red_carpet']
        for key, cart_item in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                cart_items.append(int(cart_item))
        items = cart.cart_items.filter(status='pending')
        items.update(is_selected=False)
        items = items.filter(id__in=cart_items)
        items.update(is_selected=True)
        total_price = 0
        for item in items:
            total_price += item.total_price_product
        return redirect(reverse('select_address'))
