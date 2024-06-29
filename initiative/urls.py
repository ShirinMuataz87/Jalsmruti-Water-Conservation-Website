"""
URL configuration for the initiative app.

The `urlpatterns` list routes URLs to views. For more information, please see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from initiative.views import PostView, InitiativeView

app_name = "initiative"

urlpatterns = [path("", InitiativeView.as_view(), name='initiative_index'),
               path("<int:pk>/<slug:slug>", PostView.as_view(), name='post_detail'), ]

# Adding static files URL patterns
urlpatterns += staticfiles_urlpatterns()
