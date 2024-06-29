from django.db import models
from utility.base_models import BaseSection, BasePost


class InitiativeSection(BaseSection):
    """
    Model representing a section of an initiative.
    Inherits common fields and methods from BaseSection.
    """
    pass


class Post(BasePost):
    """
    Model representing a post within an initiative section.
    Inherits common fields and methods from BasePost.

    Attributes:
        long_description (str): A longer description of the post, optional.
        button (str): Text for an associated button, optional.
        button_url (str): URL for the associated button, optional.
        quote (str): A relevant quote for the post, optional.
        region (str): Geographic region related to the post, optional.
        visit_button (str): Text for a visit button, optional.
        created_on (datetime): The date and time the post was created.
    """
    long_description = models.CharField(max_length=255, blank=True)
    button = models.CharField(max_length=200, blank=True)
    button_url = models.CharField(max_length=200, blank=True)
    quote = models.CharField(max_length=200, blank=True)
    region = models.CharField(max_length=200, blank=True)
    visit_button = models.CharField(max_length=100, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
