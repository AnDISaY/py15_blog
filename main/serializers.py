from rest_framework import serializers

from .models import Category, Post, PostImage, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# class PostDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name')

    class Meta:
        model = Post
        fields = ['id', 'title', 'user', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(allow_empty_file=False
                                                                ))

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        images = validated_data.pop('images')
        post = super().create(validated_data)
        for image in images:
            PostImage.objects.create(post=post, image=image)
        return post

    def update(self, instance, validated_data):
        images = validated_data.pop('images')
        if images:
            for image in images:
                PostImage.objects.create(post=instance, image=image)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation()
        return representation


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
