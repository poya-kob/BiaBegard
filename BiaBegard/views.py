from django.shortcuts import render
from content.models import Category
from account.forms import LoginForm, RegisterForm


# header code behind

def header(request, *args, **kwargs):

    context = {
        'categories': Category.objects.all(),

    }

    return render(request, 'shared/header.html', context)


# footer code behind
def footer(request, *args, **kwargs):

    context = {
        'login_form': LoginForm(request.POST or None),
        'register_form': RegisterForm(request.POST or None)

    }

    return render(request, 'shared/footer.html', context)
