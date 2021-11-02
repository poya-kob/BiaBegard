from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action

from .serializers import BlogListSerializer, BlogDetailSerializer, CommentsSerializer
from .models import Blog, Comments


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.filter(active=True)

    def get_serializer_class(self):

        if self.action == 'list':
            return BlogListSerializer
        else:
            return BlogDetailSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def get_queryset(self):
        print(self.kwargs)
        return super().get_queryset()
