from django.db import models
from utility.base_models import BaseSection, BasePost


class InsightSection(BaseSection):
    """
    Model representing a section of insights.
    """
    pass


class Post(BasePost):
    """
    Model representing a post in the insight section.

    Attributes:
        author (str): The author of the post.
        category (str): The category of the post.
        topic (str): The topic of the post.
        region (str): The region related to the post (optional).
        created_on (DateTimeField): The date and time the post was created.
    """
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=255)
    topic = models.CharField(max_length=200)
    region = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
