from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text

from .models import Customers, Suppliers, Subscribers
from .forms import LoginForm, RegisterForm
from verification_email_token_gen import account_activation_token


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

            user = Suppliers.objects.create_user(username=username, email=email, password=password, phone=phone,
                                                 is_staff=True,
                                                 is_active=False)
            current_site = get_current_site(request)
            mail_subject = 'اکانت خود را در بیابگرد فعال کنید.'
            message = render_to_string('verification_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [email, ])

        else:
            Customers.objects.create_user(username=username, email=email, password=password, phone=phone,
                                          is_staff=False,
                                          is_active=True)
    # todo show success message and redirect to the next url
    return redirect('/')


def email_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Suppliers.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Suppliers.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def register_subscriber(request):
    if request.method == "POST":
        email = request.POST.get('EMAIL')
        Subscribers.objects.create(email=email)
    return redirect('/')
