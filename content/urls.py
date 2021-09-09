from django.urls import path
from .views import ProductsList, DetailProduct

urlpatterns = [
    path('', ProductsList.as_view(), name='products'),
    path('<int:pk>/', DetailProduct.as_view()),

]
