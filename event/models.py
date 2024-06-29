from django.db import models
from utility.base_models import BaseSection, BasePost


class EventSection(BaseSection):
    """
    Model representing a section of an event.
    Inherits common fields and functionality from BaseSection.
    """
    pass


class Post(BasePost):
    """
    Model representing a post within an event section.

    Attributes:
        type (str): The type of the post.
        category (str): The category of the post.
        created_on (date): The date the post was created.
        start_time (time): The start time of the event.
        end_time (time): The end time of the event.
        mode (str): The mode of the event (e.g., online, offline).
    """
    type = models.CharField(max_length=200)
    category = models.CharField(max_length=255)
    created_on = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    mode = models.CharField(max_length=200)
