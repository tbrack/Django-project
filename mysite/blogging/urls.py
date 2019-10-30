from blogging.views import list_view, detail_view, UserViewSet, GroupViewSet, PostViewSet, CategoryViewSet
from django.urls import path, include
from rest_framework import routers
from blogging.feeds import BlogFeed


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('latest/feed/', BlogFeed())
]
