"""
URL configuration for the home app.

The `urlpatterns` list routes URLs to views. For more information, see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.urls import path
from home.views import IndexView, AboutView, ContactFormView

app_name = "home"

urlpatterns = [path("", IndexView.as_view(), name="index"),
               path('contact_form/', ContactFormView.as_view(), name='contact_form'),
               path("about/", AboutView.as_view(), name="about")]
