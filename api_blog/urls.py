from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from .views import BlogViewSet, CommentViewSet

# comments_list = CommentViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# comments_detail = CommentViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

router = SimpleRouter()
router.register('blog', BlogViewSet, basename='blog')
domains_router = routers.NestedSimpleRouter(router, r'blog', lookup='blog')
domains_router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(domains_router.urls)),
    # path('blog/<int:id>/comments/', comments_list, name="comments_list"),
    # path('blog/<int:id>/comments/<int:pk>', comments_detail, name="comments-detail"),

]
