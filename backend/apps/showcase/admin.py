from django.contrib import admin
from .models import CoverImage, GalleryItem, AuthorAvatar, AuthorInfo


class SingletonAdmin(admin.ModelAdmin):
    """单例模型管理基类"""

    def has_add_permission(self, request):
        # 如果已存在记录，不允许添加新记录
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # 避免误删，限制删除
        return False


@admin.register(CoverImage)
class CoverImageAdmin(SingletonAdmin):
    list_display = ("title", "subtitle")
    fieldsets = (
        ("封面图片", {
            "fields": ("url", "file"),
            "description": "封面背景图片（可上传本地文件或使用外部链接）",
        }),
        ("封面文字", {
            "fields": ("title", "subtitle"),
            "description": "封面标题与副标题",
        }),
    )


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    fieldsets = (
        ("作品信息", {
            "fields": ("file", "image", "title", "description"),
            "description": "可上传本地图片或使用外部链接",
        }),
        ("设置", {
            "fields": ("order", "is_active"),
        }),
    )


@admin.register(AuthorAvatar)
class AuthorAvatarAdmin(SingletonAdmin):
    list_display = ("__str__",)
    fieldsets = (
        ("作者头像", {
            "fields": ("file", "url"),
            "description": "可上传本地图片或使用外部链接",
        }),
    )


@admin.register(AuthorInfo)
class AuthorInfoAdmin(SingletonAdmin):
    list_display = ("name",)
    fieldsets = (
        ("作者信息", {
            "fields": ("name", "description"),
            "description": "设置作者姓名与简介",
        }),
    )
