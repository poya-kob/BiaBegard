from django.urls import path, include
from .views import ProductsList, DetailProduct, ProductSearch
from rest_framework.routers import SimpleRouter
from content.api.api_views import ProductViewset

router = SimpleRouter()
router.register(r'product-viewset', ProductViewset, basename='products')


urlpatterns = [
    path('', ProductsList.as_view(), name='products'),
    path('<int:pk>/', DetailProduct.as_view(), name='product-detail'),
    path('<int:pk>/<str:title>/', DetailProduct.as_view(), name='product-detail'),
    path('products/search', ProductSearch.as_view(), name='search'),
    path('', include(router.urls)),

]
