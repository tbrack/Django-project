from blogging.views import list_view, stub_view
from django.urls import path

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', stub_view, name="blog_detail"),
]
