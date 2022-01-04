# TODO: список категорий    #
# TODO: CRUD постов         #
# TODO: добавить картинки   #
# TODO: комменты
# TODO: подключить twilio
# TODO: авторизация
# TODO: избранное, лайки
from rest_framework.generics import ListAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Category, Post, Comment
from .permissions import IsAuthor
from .serializers import CategorySerializer, PostSerializer, PostListSerializer, CommentSerializer


class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            serializer_class = PostListSerializer
        return serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        return []


class CommentViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
