from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"gallery-items", views.GalleryItemViewSet, basename="gallery-item")

urlpatterns = [
    path("cover-image/", views.CoverImageDetailView.as_view(), name="cover-image"),
    path("cover-text/", views.CoverTextView.as_view(), name="cover-text"),
    path("author-avatar/", views.AuthorAvatarView.as_view(), name="author-avatar"),
    path("author-info/", views.AuthorInfoView.as_view(), name="author-info"),
    path("", include(router.urls)),
]
