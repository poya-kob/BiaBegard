from django.shortcuts import render

from account.forms import LoginForm, RegisterForm
from content.models import Category, Brands
from slider.models import Slider
from financial.models import Orders


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
        'orders': Orders.objects.filter(user_id=request.user.id, is_payed=False).first(),
    }
    return render(request, 'shared/header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {
        'login_form': LoginForm(request.POST or None),
        'register_form': RegisterForm(request.POST or None)

    }

    return render(request, 'shared/footer.html', context)
