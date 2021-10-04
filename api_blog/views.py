from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action

from .serializers import BlogListSerializer, BlogDetailSerializer
from .models import Blog


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.filter(active=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogListSerializer
        else:
            return BlogDetailSerializer

    @action(detail=True, methods=['POST', 'GET'], url_path='make-comment')
    def make_comment(self, request, pk):
        pass
