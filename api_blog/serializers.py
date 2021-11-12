from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers

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


class CommentsSerializer(HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()
    # blog = serializers.StringRelatedField()

    class Meta:
        model = Comments
        fields = "__all__"


class BlogDetailSerializer(ModelSerializer):
    comment = CommentsSerializer(many=True)

    class Meta:
        model = Blog
        exclude = ['active', 'category']
