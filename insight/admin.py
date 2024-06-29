from django.contrib import admin
from insight.models import InsightSection, Post
from utility.base_admin import NameAdmin, UrlSlugAdmin


@admin.register(InsightSection)
class InsightSectionAdmin(NameAdmin):
    """
    Admin interface options for the InsightSection model.
    """
    pass


@admin.register(Post)
class PostAdmin(UrlSlugAdmin):
    """
    Admin interface options for the Post model.
    """
    pass
