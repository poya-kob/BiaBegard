from django.shortcuts import render

# Create your views here.
from .forms import CreateContactForm
from .models import ContactUs


def contact_us(request):

    contact_form = CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')

        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        # todo: show user success message

        contact_form = CreateContactForm()
    context = {
        'contact_form': contact_form
    }

    return render(request, 'contact_us/contact_us_page.html', context)
