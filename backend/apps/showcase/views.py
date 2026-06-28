from rest_framework import viewsets, generics
from .models import CoverImage, GalleryItem, AuthorAvatar, AuthorInfo
from .serializers import (
    CoverImageSerializer, GalleryItemSerializer,
    AuthorAvatarSerializer, AuthorInfoSerializer
)


class CoverDetailView(generics.RetrieveUpdateAPIView):
    """封面设置（单例获取/更新）"""
    queryset = CoverImage.objects.all()
    serializer_class = CoverImageSerializer

    def get_object(self):
        return CoverImage.objects.first()


class GalleryItemViewSet(viewsets.ModelViewSet):
    """作品列表（增删改查）"""
    queryset = GalleryItem.objects.filter(is_active=True)
    serializer_class = GalleryItemSerializer
    ordering = ["order"]


class AuthorAvatarView(generics.RetrieveUpdateAPIView):
    """作者头像（单例获取/更新）"""
    queryset = AuthorAvatar.objects.all()
    serializer_class = AuthorAvatarSerializer

    def get_object(self):
        return AuthorAvatar.objects.first()


class AuthorInfoView(generics.RetrieveUpdateAPIView):
    """作者信息（单例获取/更新）"""
    queryset = AuthorInfo.objects.all()
    serializer_class = AuthorInfoSerializer

    def get_object(self):
        return AuthorInfo.objects.first()
