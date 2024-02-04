from django.urls import path
from django.contrib import admin
from django.urls import include

from . import views

urlpatterns = [
     path("", views.ReviewView.as_view()),
     path("thank-you", views.ThankYouView.as_view()),
     path("review-list", views.ReviewListView.as_view()),
     path("profiles/", include("profiles.urls")),
     path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="single-review")
]
