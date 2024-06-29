from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render
from event.models import EventSection, Post
from utility.base_views import BaseView


class EventView(BaseView):
    template_name = 'event/event_index.html'

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for the event index page.

        Args:
            request: The HTTP request object.

        Returns:
            HttpResponse: The rendered event index page.
        """
        try:
            event = EventSection.objects.get(name="Event Section")
        except EventSection.DoesNotExist:
            event = None

        try:
            posts = Post.objects.all().order_by('-created_on')
        except Post.DoesNotExist:
            posts = None

        image_url = event.image.url if event and event.image else settings.DEFAULT_IMAGE_URL
        self.meta = self.get_meta(event.title if event else "Events",
                                  event.description if event else "",
                                  event.keywords if event else "",
                                  '/event/', image_url)
        data = {"event": event,
                "posts": posts,
                'meta': self.meta,
                'style': "page-node-type-simple-page"}
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)


class PostView(BaseView):
    template_name = 'event/event_post.html'

    def get(self, request, pk, slug, *args, **kwargs):
        """
        Handle GET requests for individual event posts.

        Args:
            request: The HTTP request object.
            pk (int): The primary key of the post.
            slug (str): The URL slug of the post.

        Returns:
            HttpResponse: The rendered post page or 404 if not found.
        """
        try:
            post = Post.objects.get(pk=pk)
            if slug != post.url_slug:
                return HttpResponseNotFound()
        except Post.DoesNotExist:
            return HttpResponseNotFound()

        self.meta = self.get_meta(f"{post.title} | {settings.META_EVENT_SITE_NAME}",
                                  post.description, post.keywords,
                                  f'/event/{pk}/{slug}/',
                                  post.image.url)
        data = {"post": post,
                'meta': self.meta
                }
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)