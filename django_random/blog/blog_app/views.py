from django.shortcuts import render
from .models import Post, User
from django.http import HttpResponse, request
from django.views import View


class AllPostsView(View):
    def get(self, request):
        posts = Post.objects.all()

        return render(request, 'blog_app/all_posts.html', {'posts': posts})


class PostDetailsView(View):
    def get(self, request, id_):
        post_detail = Post.objects.get(id=id_)

        return render(request, 'blog_app/post_details.html', {'details': post_detail})
