from django.http import HttpResponseNotFound
from django.shortcuts import render
from initiative.models import InitiativeSection, Post
from jalsmruti import settings
from utility.base_views import BaseView


class InitiativeView(BaseView):
    """
    View for displaying the initiative index page.

    Attributes:
        template_name (str): The name of the template to render.
        knowledge (dict): Context data to pass to the template.
        meta (Meta): Metadata for the initiative page.
    """
    template_name = 'initiative/initiative_index.html'

    def get(self, request):
        """
        Handle GET requests for the initiative index page.

        Args:
            request: The HTTP request object.

        Returns:
            HttpResponse: The rendered initiative index page.
        """
        try:
            initiative = InitiativeSection.objects.get(name="Initiative Section")
        except InitiativeSection.DoesNotExist:
            initiative = None

        try:
            posts = Post.objects.all().order_by('-created_on')
        except Post.DoesNotExist:
            posts = None

        image_url = initiative.image.url if initiative and initiative.image else settings.DEFAULT_IMAGE_URL
        self.meta = self.get_meta(initiative.title if initiative else "Initiatives",
                                  initiative.description if initiative else "",
                                  initiative.keywords if initiative else "", '/initiative/',
                                  image_url)
        data = {"initiative": initiative,
                "posts": posts,
                'meta': self.meta,
                'style': "transparent-header white initiatives path-node page-node-type-page"}
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)


class PostView(BaseView):
    """
    View for displaying individual initiative posts.

    Attributes:
        template_name (str): The name of the template to render.
        knowledge (dict): Context data to pass to the template.
        meta (Meta): Metadata for the post page.
    """
    template_name = 'initiative/initiative_post.html'

    def get(self, request, pk, slug):
        """
        Handle GET requests for individual initiative posts.

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

        self.meta = self.get_meta(f"{post.title} | {settings.META_INITIATIVE_SITE_NAME}",
                                  post.description,
                                  post.keywords, f'/initiative/{pk}/{slug}/',
                                  post.image.url)
        data = {"post": post,
                'meta': self.meta,
                'style': "transparent-header white path-node page-node-type-project-detail"}
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)