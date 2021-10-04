from django.shortcuts import render

from account.forms import LoginForm, RegisterForm
from content.models import Category, Brands
from slider.models import Slider
from financial.models import Carts


def home_page(request):
    sliders = Slider.objects.all()
    brands = Brands.objects.all()

    context = {
        'sliders': sliders,
        'brands': brands
    }

    return render(request, 'home.html', context)


# header code behind

def header(request, *args, **kwargs):
    context = {
        'categories': Category.objects.all().order_by('parent'),

    }
    if request.user.is_authenticated:
        total_price = 0
        orders = Carts.objects.filter(user_id=request.user.id).first()
        if orders:
            for order in orders.cart_items.filter(status="pending"):
                total_price += order.total_price_product
            context['orders'] = orders
            context['total_price'] = total_price
            context['total_item'] = orders.cart_items.filter(status="pending").count()

    return render(request, 'shared/header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {
        'login_form': LoginForm(request.POST or None),
        'register_form': RegisterForm(request.POST or None)

    }

    return render(request, 'shared/footer.html', context)
