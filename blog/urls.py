from django.urls import path
from blog.views import (
    BlogListView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogDetailView,
)
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("blog/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/<slug:slug>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<slug:slug>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
