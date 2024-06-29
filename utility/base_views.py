from django.utils.html import strip_tags
from django.views.generic import TemplateView
from meta.views import Meta
from django.conf import settings


def remove_html(text):
    """
    Remove HTML tags from the given text.

    Args:
        text (str): The text to strip HTML tags from.

    Returns:
        str: Text without HTML tags.
    """
    return strip_tags(text)


def string_to_list(string):
    """
    Convert a comma-separated string into a list.

    Args:
        string (str): The comma-separated string.

    Returns:
        list: The list of strings.
    """
    return list(string.split(", "))


class BaseView(TemplateView):
    """
    Base view for handling common functionality.
    """
    knowledge = {}
    meta = None

    def get_meta(self, title, description, keywords, url, image):
        """
        Generate meta tags for the page.

        Args:
            title (str): The title of the page.
            description (str): The description of the page.
            keywords (str): The keywords for the page.
            url (str): The URL of the page.
            image (str): The image URL for the page.

        Returns:
            Meta: The Meta object with the given properties.
        """
        return Meta(
            use_title_tag=True,
            use_og=True,
            use_twitter=True,
            use_facebook=True,
            title=title,
            description=remove_html(description),
            keywords=string_to_list(keywords),
            url=url,
            image=image,
            object_type='website',
            site_name=settings.META_EVENT_SITE_NAME,
            twitter_site=settings.META_TWITTER_SITE,
            twitter_creator=settings.META_TWITTER_CREATOR,
            twitter_type='summary_large_image',
        )