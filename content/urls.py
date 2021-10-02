from django.urls import path
from .views import ProductsList, DetailProduct, ProductSearch

urlpatterns = [
    path('', ProductsList.as_view(), name='products'),
    path('<int:pk>/', DetailProduct.as_view(), name='product-detail'),
    path('<int:pk>/<str:title>/', DetailProduct.as_view(), name='product-detail'),
    path('products/search', ProductSearch.as_view(), name='search'),

]
