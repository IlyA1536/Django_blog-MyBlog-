from django.shortcuts import render
from blog.models import Post, Author


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
    time_delta = post.published_recently()
    context = {
        "post": post,
        "published_test": time_delta,
    }
    return render(
        request,
        "blog/post.html",
        context,

    )

def author_posts(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "posts": author.posts.all(),
    }
    return render(
        request,
        "blog/author_posts.html",
        context,
    )
