from django.utils.deprecation import MiddlewareMixin

from .models import Suppliers, Customers


class UserObject(MiddlewareMixin):
    def process_request(self, request):
        request.user_obj = None
        if request.user.is_authenticated:
            if request.session['user_type'] == "customer":
                request.user_obj = Customers.objects.get(username=request.user.username, password=request.user.password)
            elif request.session['user_type'] == "supplier":
                request.user_obj = Suppliers.objects.get(username=request.user.username, password=request.user.password)
