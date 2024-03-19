from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from .models import *
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm


all_posts = Post.objects.all()

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    


# Function based views below

# def get_date(post):
#     return post['date']

# def starting_page(request):
#     latest_posts = all_posts.order_by("-date")[:3]
#     context = {"posts": latest_posts}

#     return render(request, "blog/index.html", context)
    
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


# def posts_page(request):
#     context = {"all_posts": all_posts}
#     return render(request, "blog/all-posts.html", context)

# def post_detail(request, slug):
#     selected_post = Post.objects.get(slug=slug)
#     context = {"post": selected_post, "post_tags": selected_post.tag.all()}
#     return render(request, "blog/post-detail.html", context)

class SinglePostView(View):
    def is_stored_post(self, request, post_id): #you will get post_id as a url parameter
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "saved_for_later":self.is_stored_post(request, post.id) #super important line i just added to complete the is_stored_post() function above (LECTURE 200)
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False) #will not hit the Database right away (this is good practice anyway)
            comment.post=post #see lecture 192 why this is needed.
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug])) #this will redirect back to detail page but will call GET method!        
       
        context = {
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later":self.is_stored_post(request, post.id) #super important line i just added to complete the is_stored_post() function above (LECTURE 200)

        }
        return render(request, "blog/post-detail.html", context)
    
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts) #"__" is a special modifier
            context["posts"] = posts
            context["has_posts"] = True
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")

        
        
