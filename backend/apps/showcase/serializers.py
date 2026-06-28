from rest_framework import serializers
from .models import CoverImage, CoverText, GalleryItem, AuthorAvatar, AuthorInfo


class CoverImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CoverImage
        fields = ["id", "url", "file", "image_url"]

    def get_image_url(self, obj):
        if obj.file:
            return obj.file.url
        return obj.url


class CoverTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverText
        fields = "__all__"


class GalleryItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = GalleryItem
        fields = ["id", "image", "file", "title", "description", "order", "is_active", "image_url"]

    def get_image_url(self, obj):
        if obj.file:
            return obj.file.url
        return obj.image


class AuthorAvatarSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = AuthorAvatar
        fields = ["id", "url", "file", "image_url"]

    def get_image_url(self, obj):
        if obj.file:
            return obj.file.url
        return obj.url


class AuthorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorInfo
        fields = "__all__"
