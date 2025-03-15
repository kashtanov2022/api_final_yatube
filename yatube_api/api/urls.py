from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, FollowViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('follow/', FollowViewSet.as_view({'get': 'list', 'post': 'create'})),
]
