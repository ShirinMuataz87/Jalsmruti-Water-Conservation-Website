"""
URL configuration for the team app.

The `urlpatterns` list routes URLs to views. For more information, please see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from team.views import PostView, TeamView

app_name = "team"

urlpatterns = [path("", TeamView.as_view(), name='team_index'),
               path("<int:pk>/<slug:slug>", PostView.as_view(), name='post_detail')]

# Adding static files URL patterns
urlpatterns += staticfiles_urlpatterns()
