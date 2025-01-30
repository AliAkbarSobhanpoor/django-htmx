from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from blog.models import Post

# Create your views here.


def index(request: HttpRequest):
    blog_posts:Post = Post.objects.all()
    context:dict = {
        'blog_posts': blog_posts
    }
    return render(request, 'blog/index.html', context=context)


def archive_blog_post(request, post_id):
    post:Post = get_object_or_404(Post, id=post_id)
    post.ia_archived = True
    post.save()
    return redirect('blog_index')


def restore_blog_post(request, post_id):
    post:Post = get_object_or_404(Post, id=post_id)
    post.ia_archived = False
    post.save()
    return redirect('blog_index')