from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import BlogViewSet, CommentViewSet

router = SimpleRouter()
router.register('blog', BlogViewSet, basename='blog')
router.register('blog/<int:id>/comments', CommentViewSet, basename='comments')
urlpatterns = [
    path('', include(router.urls)),

]
