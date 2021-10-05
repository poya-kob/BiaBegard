from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import UserNewOrderForm
from .models import Carts, CartItems


@login_required(login_url='/#loginModal')
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
            cart_item.qty += count
            cart_item.save()
        else:
            cart.cart_items.create(product_id=product_id, qty=count)

    return redirect('/')


@login_required(login_url='/#loginModal')
def delete_user_order(request):
    CartItems.objects.get(id=request.GET.get('id')).delete()
    return redirect('/')


@login_required(login_url='/#loginModal')
def check_out_step1(request):
    cart_items = Carts.objects.filter(user_id=request.user.id).first()
    total_price = 0
    for item in cart_items.cart_items.filter(status='pending'):
        total_price += item.total_price_product
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'financial/check_to_pay.html', context)


@login_required(login_url='/#loginModal')
def pay_page(request):
    items = None
    context = {}
    cart = Carts.objects.get(user_id=request.user.id)
    if request.POST:
        cart_items = []
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
        context['cart_items'] = items
        context['total_price'] = total_price
        return render(request, 'financial/pay_item.html', context)
    items = cart.cart_items.filter(status='pending', is_selected=True)
    total_price = 0
    for item in items:
        total_price += item.total_price_product
    context['cart_items'] = items
    context['total_price'] = total_price
    return render(request, 'financial/pay_item.html', context)
