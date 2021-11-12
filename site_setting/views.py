from django.shortcuts import render


def about_us(request):
    return render(request, 'site_setting/about_us.html')
