from django.shortcuts import render, redirect
from .models import Customers,Suppliers
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    context = {
        'login_form': login_form,
        'title': 'ورود | بیابگرد'
    }

    if login_form.is_valid():
        username = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'shared/header.html', context)


def logout_page(request):
    logout(request)
    return redirect("/")


def register_page(request):

    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        # username = register_form.cleaned_data.get('user_name')
        # email = register_form.cleaned_data.get('email')
        # password = register_form.cleaned_data.get('password')
        # User.objects.create_user(username=username, email=email, password=password)
        #TODO REGISTER_USER
        return redirect('/login')

    context = {
        'register_form': register_form,
        'title': 'ثبت نام | فروشگاه آزمایشی'
    }
    # return render(request, 'account/register.html', context)
