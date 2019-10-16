from blogging.views import stub_view
from django.urls import path

urlpatterns = [
    path('', stub_view, name="blog_index"),
]