from django.urls import path

from .views import add_user_order

urlpatterns = [
    path('add-user-order', add_user_order, name="add_user_order"),
]
