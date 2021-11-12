from .models import SiteSetting


def context_setting(request):
    if SiteSetting.objects.count() > 0:
        return {'setting': SiteSetting.objects.first()}
    else:
        return {'setting': None}
