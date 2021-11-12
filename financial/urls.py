from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import add_user_order, check_out_step1, delete_user_order, pay_page, SelectAddress, GetSelectedCartItems

urlpatterns = [
    path('add-user-order/', add_user_order, name="add_user_order"),
    path('remove-item/', delete_user_order, name="remove-item"),
    path('check/', check_out_step1, name="check_step1"),
    path('pay/', pay_page, name="pay_page"),
    path('select-address/', login_required(SelectAddress.as_view()), name="select_address"),
    path('select-cart-item/', login_required(GetSelectedCartItems.as_view()), name="select-cart-item"),
]
