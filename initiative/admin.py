from django.contrib import admin
from initiative.models import InitiativeSection, Post
from utility.base_admin import NameAdmin, UrlSlugAdmin


@admin.register(InitiativeSection)
class InitiativeSectionAdmin(NameAdmin):
    """
    Admin interface options for the InitiativeSection model.
    Inherits from NameAdmin to provide read-only 'name' field and
    to disable add and delete functionality.
    """
    pass


@admin.register(Post)
class PostAdmin(UrlSlugAdmin):
    """
    Admin interface options for the Post model.
    Inherits from UrlSlugAdmin to provide read-only 'url_slug' field.
    """
    pass
