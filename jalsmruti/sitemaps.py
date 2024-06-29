from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from initiative.models import Post as InitiativePost
from insight.models import Post as InsightPost
from event.models import Post as EventPost
from team.models import Post as TeamPost


class StaticSitemap(Sitemap):
    """Sitemap for static pages."""
    changefreq = "monthly"
    priority = 1.0
    protocol = 'https'

    def items(self):
        """Returns a list of static page names."""
        return [
            'home:index',
            'home:about',
            'initiative:initiative_index',
            'insight:insight_index',
            'event:event_index',
            'team:team_index'
        ]

    def location(self, item):
        """Returns the URL of the given item."""
        return reverse(item)


class BasePostSitemap(Sitemap):
    """Base sitemap class for post models."""
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def lastmod(self, obj):
        """Returns the last modified date of the given post."""
        return obj.last_modified

    def location(self, obj):
        """Returns the URL of the given post."""
        return f'/{self.section}/{obj.pk}/{obj.url_slug}'


class InitiativePostSitemap(BasePostSitemap):
    """Sitemap for initiative posts."""
    section = 'initiative'

    def items(self):
        """Returns all initiative posts."""
        return InitiativePost.objects.all()


class InsightPostSitemap(BasePostSitemap):
    """Sitemap for insight posts."""
    section = 'insight'

    def items(self):
        """Returns all insight posts."""
        return InsightPost.objects.all()


class EventPostSitemap(BasePostSitemap):
    """Sitemap for event posts."""
    section = 'event'

    def items(self):
        """Returns all event posts."""
        return EventPost.objects.all()


class TeamPostSitemap(BasePostSitemap):
    """Sitemap for team posts."""
    section = 'team'

    def items(self):
        """Returns all team posts."""
        return TeamPost.objects.all()