from django.urls import path
from .views import payment_start,payment_return

urlpatterns = [

    path('payment-start/', payment_start, name="payment_start"),
    path('payment-return/', payment_return, name="payment_return"),
]
