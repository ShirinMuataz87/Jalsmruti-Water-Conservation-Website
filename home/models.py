from django.db import models
from ckeditor.fields import RichTextField
from utility.base_models import BaseSection


class HomeSection(BaseSection):
    """
    Model representing a section of the home page.

    Attributes:
        challenge (RichTextField): The challenge description for the home section.
        approach (RichTextField): The approach description for the home section.
    """
    challenge = RichTextField(config_name="default")
    approach = RichTextField(config_name="default")


class Fact(models.Model):
    """
    Model representing a fact with a percentage.

    Attributes:
        facts (str): The fact description.
        percentage (int): The percentage value of the fact.
    """
    facts = models.CharField(max_length=255)
    percentage = models.IntegerField()

    def __str__(self):
        """Return a string representation of the fact."""
        return self.facts


class SocialMedia(models.Model):
    """
    Model representing a social media link.

    Attributes:
        name (str): The name of the social media platform.
        url (str): The URL of the social media profile.
    """
    name = models.CharField(max_length=255)
    url = models.TextField(max_length=150, blank=True)

    def __str__(self):
        """Return a string representation of the social media platform."""
        return self.name


class Message(models.Model):
    """
    Model representing a contact message.

    Attributes:
        email (str): The email address of the sender.
        name (str): The name of the sender.
        query (str): The message/query from the sender.
        receive_newsletter (bool): Whether the sender wants to receive the newsletter.
    """
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=255, blank=True)
    query = models.CharField(max_length=1000, blank=True)
    receive_newsletter = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the email address."""
        return self.email


class AboutPage(BaseSection):
    """
    Model representing the about page details.

    Attributes:
        challenges (RichTextField): The challenges description for the about page.
        vision_mission (RichTextField): The vision and mission description for the about page.
        services (RichTextField): The services description for the about page.
        team (RichTextField): The team description for the about page.
        team_image (ImageField): The team image for the about page.
    """
    challenges = RichTextField(config_name="default")
    vision_mission = RichTextField(config_name="default")
    services = RichTextField(config_name="default")
    team = RichTextField(config_name="default")
    team_image = models.ImageField(upload_to='images/')


class Image(models.Model):
    """
    Model representing an image.

    Attributes:
        name (str): The name of the image.
        image (ImageField): The image file.
    """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        """Return a string representation of the image name."""
        return self.name
