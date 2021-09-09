from django.shortcuts import redirect
from .models import Customers, Suppliers
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    context = {
        'login_form': login_form,
    }
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('/')


def logout_page(request):
    logout(request)
    return redirect("/")


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        phone = register_form.cleaned_data.get('phone')
        password = register_form.cleaned_data.get('password')

        if register_form.cleaned_data.get('be_supplier'):
            Suppliers.objects.create_user(username=username, email=email, password=password, phone=phone, is_staff=True,
                                          is_active=False)
        Customers.objects.create_user(username=username, email=email, password=password, phone=phone, is_staff=False,
                                      is_active=True)
    # todo show success message and redirect to the next url
    return redirect('/')
