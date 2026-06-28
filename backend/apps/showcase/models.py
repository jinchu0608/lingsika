from django.db import models


class CoverImage(models.Model):
    """封面设置（单例）"""
    title = models.CharField(
        max_length=200,
        help_text="封面主标题",
        default="影像集"
    )
    subtitle = models.CharField(
        max_length=500,
        help_text="封面副标题",
        default="每一帧都是时光的标本",
        blank=True
    )
    file = models.ImageField(
        upload_to="covers/",
        blank=True,
        null=True,
        help_text="上传本地图片（优先于外部链接）"
    )
    url = models.URLField(
        max_length=500,
        help_text="封面背景图片链接",
        default="https://picsum.photos/seed/photography-hero/1920/1080"
    )

    class Meta:
        verbose_name = "封面设置"
        verbose_name_plural = "封面设置"

    def __str__(self):
        return f"封面：{self.title}"


class GalleryItem(models.Model):
    """作品展示项"""
    file = models.ImageField(
        upload_to="gallery/",
        blank=True,
        null=True,
        help_text="上传本地图片（优先于外部链接）"
    )
    image = models.URLField(
        max_length=500,
        help_text="作品图片链接",
        default="https://picsum.photos/seed/gallery/800/600"
    )
    title = models.CharField(max_length=200, help_text="作品标题")
    description = models.TextField(help_text="作品描述", blank=True)
    order = models.IntegerField(default=0, help_text="排序编号（数字越小越靠前）")
    is_active = models.BooleanField(default=True, help_text="是否显示")

    class Meta:
        ordering = ["order"]
        verbose_name = "作品"
        verbose_name_plural = "作品列表"

    def __str__(self):
        return self.title


class AuthorAvatar(models.Model):
    """作者头像（单例）"""
    file = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
        help_text="上传本地图片（优先于外部链接）"
    )
    url = models.URLField(
        max_length=500,
        help_text="头像图片链接",
        default="https://picsum.photos/seed/photographer/200/200"
    )

    class Meta:
        verbose_name = "作者头像"
        verbose_name_plural = "作者头像"

    def __str__(self):
        return "作者头像" + ("[本地]" if self.file else "[外链]")


class AuthorInfo(models.Model):
    """作者姓名与简介（单例）"""
    name = models.CharField(max_length=200, help_text="作者姓名", default="摄影师")
    description = models.TextField(
        help_text="作者简介",
        default="热爱摄影，用镜头捕捉生活中的美好瞬间。"
    )

    class Meta:
        verbose_name = "作者信息"
        verbose_name_plural = "作者信息"

    def __str__(self):
        return f"作者信息：{self.name}"
