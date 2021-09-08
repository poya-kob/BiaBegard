from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .form import RegisterForm

# Create your views here.
def register_page(request):

    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login')

    context = {
        'register_form': register_form,
        'title': 'ثبت نام | فروشگاه آزمایشی'
    }
    # return render(request, 'account/register.html', context)
