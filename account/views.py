from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


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
    return render(request, 'account/login.html', context)


def logout_page(request):
    logout(request)
    return redirect("/")
