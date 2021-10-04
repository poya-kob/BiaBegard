from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import BlogViewSet

router = SimpleRouter()
router.register('blog', BlogViewSet, basename='blog')
urlpatterns = [
    path('', include(router.urls))
]
