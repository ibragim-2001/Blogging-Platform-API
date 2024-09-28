from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tags', 'create_at', 'update_at')
        read_only_fields = ('create_at', 'update_at')

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)
        post.tags.set(tags)
        return tags


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'category', 'tags', 'create_at', 'update_at')
        read_only_fields = ('create_at', 'update_at')
