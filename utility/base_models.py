from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class BaseSection(models.Model):
    """
    Abstract base model representing a section with common attributes.
    """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    description = RichTextField(config_name="default")
    keywords = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BasePost(models.Model):
    """
    Abstract base model representing a post with common attributes.
    """
    title = models.CharField(max_length=200)
    url_slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    body = RichTextField(config_name="default")
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate the URL slug from the title.
        """
        if not self.url_slug:
            self.url_slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
