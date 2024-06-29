from django.http import HttpResponseNotFound
from django.shortcuts import render
from insight.models import InsightSection, Post
from jalsmruti import settings
from utility.base_views import BaseView


class InsightView(BaseView):
    """
    View for displaying the insight index page.

    Attributes:
        template_name (str): The name of the template to render.
        knowledge (dict): Context data to pass to the template.
        meta (Meta): Metadata for the insight page.
    """
    template_name = 'insight/insight_index.html'

    def get(self, request):
        """
        Handle GET requests for the insight index page.

        Args:
            request: The HTTP request object.

        Returns:
            HttpResponse: The rendered insight index page.
        """
        try:
            insight = InsightSection.objects.get(name="Insight Section")
        except InsightSection.DoesNotExist:
            insight = None

        try:
            posts = Post.objects.all().order_by('-created_on')
        except Post.DoesNotExist:
            posts = None

        image_url = insight.image.url if insight and insight.image else settings.DEFAULT_IMAGE_URL
        self.meta = self.get_meta(
            insight.title if insight else "Insights",
            insight.description if insight else "",
            insight.keywords if insight else "",
            '/insight/',
            image_url
        )
        data = {
            "insight": insight,
            "posts": posts,
            'meta': self.meta,
            'style': "transparent-header white"
        }
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)


class PostView(BaseView):
    """
    View for displaying individual insight posts.

    Attributes:
        template_name (str): The name of the template to render.
        knowledge (dict): Context data to pass to the template.
        meta (Meta): Metadata for the post page.
    """
    template_name = 'insight/insight_post.html'

    def get(self, request, pk, slug):
        """
        Handle GET requests for individual insight posts.

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

        self.meta = self.get_meta(
            f"{post.title} | {settings.META_INSIGHT_SITE_NAME}",
            post.description,
            post.keywords,
            f'/insight/{pk}/{slug}/',
            post.image.url
        )
        data = {
            "post": post,
            'meta': self.meta,
        }
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)