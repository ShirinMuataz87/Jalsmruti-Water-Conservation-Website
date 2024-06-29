from django.contrib import admin
from event.models import EventSection, Post
from utility.base_admin import NameAdmin, UrlSlugAdmin


@admin.register(EventSection)
class EventSectionAdmin(NameAdmin):
    """
    Admin interface options for the EventSection model.

    Inherits common functionalities from NameAdmin to handle
    read-only 'name' field and disable add and delete functionalities.
    """
    pass


@admin.register(Post)
class PostAdmin(UrlSlugAdmin):
    """
    Admin interface options for the Post model.

    Inherits common functionalities from UrlSlugAdmin to handle
    read-only 'url_slug' field and disable add and delete functionalities.
    """
    pass
