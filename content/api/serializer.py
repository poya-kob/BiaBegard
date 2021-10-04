from rest_framework import serializers

from content.models import Products, Category
from comment.models import Comments


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class DetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ListProductSerializer(serializers.HyperlinkedModelSerializer):
    category = DetailCategorySerializer()
    brand = serializers.StringRelatedField()

    class Meta:
        model = Products
        fields = ['name', 'url', 'inventory', 'short_description', 'product_price', 'brand', 'category']


class DetailProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Products
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     comment_data = validated_data.pop('comments')
    #     coomment = instance.comments.create(**comment_data)
    #     return coomment
    #
    # def create(self, validated_data):
    #     return Comments.objects.create(**validated_data)
