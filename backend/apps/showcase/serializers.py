from rest_framework import serializers
from .models import CoverImage, CoverText, GalleryItem, AuthorAvatar, AuthorInfo


class CoverImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverImage
        fields = "__all__"


class CoverTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverText
        fields = "__all__"


class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = "__all__"


class AuthorAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorAvatar
        fields = "__all__"


class AuthorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorInfo
        fields = "__all__"
