from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('blog/archive/api/<int:post_id>', views.archive_blog_post, name='blog_archive'),
    path('blog/restore/api/<int:post_id>', views.restore_blog_post, name='blog_restore'),
]