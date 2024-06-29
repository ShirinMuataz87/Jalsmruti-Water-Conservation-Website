from django.http import HttpResponseNotFound
from django.shortcuts import render
from team.models import TeamSection, Post
from utility.base_views import BaseView
from django.conf import settings


class TeamView(BaseView):
    """
    View for displaying the team index page.

    Attributes:
        template_name (str): The name of the template to render.
    """
    template_name = 'team/team_index.html'

    def get(self, request):
        """
        Handle GET requests for the team index page.

        Args:
            request: The HTTP request object.

        Returns:
            HttpResponse: The rendered team index page.
        """
        try:
            team = TeamSection.objects.get(name="Team Section")
        except TeamSection.DoesNotExist:
            team = None

        try:
            posts = Post.objects.all()
        except Post.DoesNotExist:
            posts = None

        image_url = team.image.url if team and team.image else settings.DEFAULT_EVENT_IMAGE_URL
        self.meta = self.get_meta(
            team.title if team else "Team",
            team.description if team else "",
            team.keywords if team else "",
            '/team/',
            image_url
        )
        data = {
            "team": team,
            "posts": posts,
            'meta': self.meta,
        }
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)


class PostView(BaseView):
    """
    View for displaying individual team posts.

    Attributes:
        template_name (str): The name of the template to render.
    """
    template_name = 'team/team_post.html'

    def get(self, request, pk, slug):
        """
        Handle GET requests for individual team posts.

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

        languages = post.language.split(", ") if post.language and post.language.strip() else None
        self.meta = self.get_meta(
            f"{post.title} | {settings.META_TEAM_SITE_NAME}",
            post.description,
            post.keywords,
            f'/team/{pk}/{slug}/',
            post.image.url
        )
        data = {
            "post": post,
            "languages": languages,
            'meta': self.meta,
        }
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)