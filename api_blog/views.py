from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action

from .serializers import BlogListSerializer, BlogDetailSerializer, CommentsSerializer
from .models import Blog, Comments


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.filter(active=True)

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'list':

            return BlogListSerializer
        else:
            return BlogDetailSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        queryset = Comments.objects.filter(blog_id=self.kwargs['blog_pk'])
        return queryset

    # def retrieve(self, request, pk=None, blog_pk=None, *args, **kwargs):
    #     self.queryset.get(pk=pk)
    #     return super().retrieve(self, request, pk=pk, blog_pk=blog_pk, *args, **kwargs)
