from django.shortcuts import render
from blog.models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    context = {
        "posts_list": posts
    }
    return render(
        template_name="blog/posts_list.html",
        context=context,
        request=request
    )

def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(
        template_name="blog/post.html",
        context=context,
        request=request
    )