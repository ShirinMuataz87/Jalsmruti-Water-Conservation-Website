from django.core.management.base import BaseCommand
from home.models import HomeSection, SocialMedia, AboutPage
from initiative.models import InitiativeSection
from insight.models import InsightSection
from event.models import EventSection
from team.models import TeamSection
from home.constants import (HOME_SECTION_DATA, INITIATIVE_SECTION_DATA, INSIGHT_SECTION_DATA, EVENT_SECTION_DATA,
                            TEAM_SECTION_DATA, SOCIAL_MEDIA_DATA, ABOUT_PAGE_DATA)


class Command(BaseCommand):
    """
    Custom Django management command to populate website data.
    """
    help = 'Populate website data'

    @staticmethod
    def _create_tags():
        """
        Creates and saves initial data for HomeSection, InitiativeSection,
        InsightSection, EventSection, TeamSection, SocialMedia, and AboutPage models
        if they do not already exist.
        """
        if not HomeSection.objects.exists():
            home_section = HomeSection(**HOME_SECTION_DATA)
            home_section.save()

        if not InitiativeSection.objects.exists():
            initiative_section = InitiativeSection(**INITIATIVE_SECTION_DATA)
            initiative_section.save()

        if not InsightSection.objects.exists():
            insight_section = InsightSection(**INSIGHT_SECTION_DATA)
            insight_section.save()

        if not EventSection.objects.exists():
            event_section = EventSection(**EVENT_SECTION_DATA)
            event_section.save()

        if not TeamSection.objects.exists():
            team_section = TeamSection(**TEAM_SECTION_DATA)
            team_section.save()

        for social_media_name in SOCIAL_MEDIA_DATA:
            if not SocialMedia.objects.filter(name=social_media_name).exists():
                social_media = SocialMedia(name=social_media_name)
                social_media.save()

        if not AboutPage.objects.exists():
            about_page = AboutPage(**ABOUT_PAGE_DATA)
            about_page.save()

    def handle(self, *args, **options):
        """
        The entry point for the command. Calls the method to create initial tags.
        """
        self._create_tags()
