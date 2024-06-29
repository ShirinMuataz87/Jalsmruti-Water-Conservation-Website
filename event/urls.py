"""
URL configuration for the event app.

The `urlpatterns` list routes URLs to views. For more information, please see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from event.views import PostView, EventView

app_name = "event"

urlpatterns = [path("", EventView.as_view(), name='event_index'),
               path("<int:pk>/<slug:slug>/", PostView.as_view(), name='post_detail'), ]

urlpatterns += staticfiles_urlpatterns()
