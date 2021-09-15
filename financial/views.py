from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserNewOrderForm
from .models import Orders


@login_required()
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        order = Orders.objects.filter(user=request.user.id, is_payed=False).first()
        if order is None:
            order = Orders.objects.create(user_id=request.user.id)
        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count <= 0:
            count = 1

        order.order_detail.create(product_id=product_id, number_of_products=count)
    return redirect('/')
