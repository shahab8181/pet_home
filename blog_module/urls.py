from django.urls import path
from .views import BlogsView, BlogDetailView


urlpatterns = [
    path('blogs/', view=BlogsView.as_view(), name='blogs-page'),
    path('blogs/<slug:cat>', view=BlogsView.as_view(), name='filterblogs-page'),
    path('blogs/single-blog/<slug:slug>', view=BlogDetailView.as_view(), name='blog-page'),
]
