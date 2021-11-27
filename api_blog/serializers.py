from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

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


# class CommentsSerializer(ModelSerializer):
class CommentsSerializer(HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()

    class Meta:
        model = Comments
        fields = "__all__"

## inam fekr konam bayad hyperlink bashe
class BlogDetailSerializer(HyperlinkedModelSerializer):
    # comment = HyperlinkedIdentityField(
    #     view_name='comments-list',
    #     lookup_url_kwarg='blog_pk'
    # )
    comment = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,  # Or add a queryset
        view_name='comments-detail',
        parent_lookup_kwargs={'blog_pk': 'blog__pk'}
        # ^-- Nameserver queryset will .filter(domain__pk=domain_pk)
        #     being domain_pk (ONE underscore) value from URL kwargs
    )

    class Meta:
        model = Blog
        exclude = ['active', 'category']
