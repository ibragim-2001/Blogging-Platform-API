from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tags', 'create_at', 'update_at')
        read_only_fields = ('create_at', 'update_at')


    def create(self, validated_data):
        tags = validated_data.pop('tags')
        category_name = validated_data.pop('category')
        category = Category.objects.get(title=category_name)
        post = Post.objects.create(category=category, **validated_data)
        post.tags.set(tags)
        return tags


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'category', 'tags', 'create_at', 'update_at')
        read_only_fields = ('create_at', 'update_at')
