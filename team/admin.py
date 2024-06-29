from django.contrib import admin
from team.models import TeamSection, Post
from utility.base_admin import NameAdmin, UrlSlugAdmin


@admin.register(TeamSection)
class TeamSectionAdmin(NameAdmin):
    """
    Admin interface options for the TeamSection model.
    """
    pass


@admin.register(Post)
class PostAdmin(UrlSlugAdmin):
    """
    Admin interface options for the Post model.
    """
    pass
