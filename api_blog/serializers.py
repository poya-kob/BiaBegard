from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Blog, BlogCategory, Comments


class CategorySerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        exclude = ['id']


class BlogListSerializer(HyperlinkedModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Blog
        exclude = ['active', 'text']


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        exclude = ['id']


class BlogDetailSerializer(ModelSerializer):
    comment = CommentsSerializer(many=True)

    class Meta:
        model = Blog
        exclude = ['active', 'category']
