from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView # this is a more succinct way of using class based views specifically to render a template.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
# Create your views here.

class ReviewView(CreateView):
  model = Review
  fields = "__all__" #although you can still create a form_class and point to your specific form if you want specific things on it.
  template_name = "reviews/review.html"
  success_url = "/thank-you" #this takes a URL, NOT an html template!

#add UPDATEVIEW and DELETEVIEW

class ThankYouView(TemplateView):
  template_name = "reviews/thank_you.html"
  
  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    context['message'] = "Message sent!"
    return context
  
class ReviewListView(ListView):
  template_name = "reviews/review_list.html"
  model = Review
  context_object_name = "reviews"
  
class SingleReviewView(DetailView):
  template_name= "reviews/single_review.html"
  model = Review


#OLD way using TemplateView:
  # def get_context_data(self, **kwargs): #the **kwargs allow you to collect the url arguments such as <int:id>
  #   context = super().get_context_data(**kwargs)
  #   review_id = kwargs["id"]  #now you just reference kwargs and assign it a name
  #   selected_review = Review.objects.get(pk=review_id)
  #   context["username"] = selected_review.user_name
  #   context["rating"] = selected_review.rating
  #   context["review_text"] = selected_review.review_text
  #   return context