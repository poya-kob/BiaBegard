from django.urls import path
from .views import products_list, ProductsList

urlpatterns = [
    path('', ProductsList.as_view()),
    # path('', products_list)

]
