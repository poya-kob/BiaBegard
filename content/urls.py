from django.urls import path
from .views import ProductsList, DetailProduct

urlpatterns = [
    path('', ProductsList.as_view(), name='products'),
    path('<int:pk>/<str:title>/', DetailProduct.as_view(), name='product-detail'),

]
