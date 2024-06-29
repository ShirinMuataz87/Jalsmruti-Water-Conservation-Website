"""
URL Configuration fot JalSmruti website

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from .sitemaps import InitiativePostSitemap, InsightPostSitemap, StaticSitemap, EventPostSitemap, TeamPostSitemap

sitemaps = {
    'static': StaticSitemap,
    'initiative': InitiativePostSitemap,
    'insight': InsightPostSitemap,
    'event': EventPostSitemap,
    'team': TeamPostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', 'home'), name='home'),
    path('initiative/', include('initiative.urls', 'initiative'), name='initiative'),
    path('insight/', include('insight.urls', 'insight'), name='insight'),
    path('event/', include('event.urls', 'event'), name='event'),
    path('team/', include('team.urls', 'team'), name='team'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
