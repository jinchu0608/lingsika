from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"gallery-items", views.GalleryItemViewSet, basename="gallery-item")

urlpatterns = [
    path("cover/", views.CoverDetailView.as_view(), name="cover"),
    path("author-avatar/", views.AuthorAvatarView.as_view(), name="author-avatar"),
    path("author-info/", views.AuthorInfoView.as_view(), name="author-info"),
    path("", include(router.urls)),
]
