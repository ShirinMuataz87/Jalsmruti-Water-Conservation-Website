from django.db import models
from utility.base_models import BaseSection, BasePost


class TeamSection(BaseSection):
    """
    Model representing a section of the team.
    Inherits from BaseSection.
    """
    pass


class Post(BasePost):
    """
    Model representing a post in the team section.
    Inherits from BasePost.

    Attributes:
        position (str): The position of the team member.
        linkedin (str): The LinkedIn profile URL of the team member.
        language (str): The language(s) spoken by the team member.
    """
    position = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
