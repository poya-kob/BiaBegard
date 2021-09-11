from django.shortcuts import render

from account.forms import LoginForm, RegisterForm

from content.models import Category


def home_page(request):
    return render(request, 'home.html')


# header code behind
def header(request, *args, **kwargs):
    context = {
        'categories': Category.objects.all().order_by('parent')
    }

    return render(request, 'shared/header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    login_form = LoginForm(request.POST or None)
    register_form = RegisterForm(request.POST or None)

    context = {
        'login_form': LoginForm(request.POST or None),
        'register_form': RegisterForm(request.POST or None)

    }

    return render(request, 'shared/footer.html', context)
