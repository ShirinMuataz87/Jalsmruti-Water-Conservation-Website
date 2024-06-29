from django.contrib import admin
from home.models import HomeSection, Fact, SocialMedia, Message, AboutPage, Image
from utility.base_admin import NameAdmin, UrlSlugAdmin, ReadOnlyAdmin


@admin.register(HomeSection)
class HomeSectionAdmin(NameAdmin):
    """
    Admin interface options for the HomeSection model.
    Inherits common functionality from NameAdmin.
    """
    pass


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Fact model.
    """
    pass


@admin.register(SocialMedia)
class SocialMediaAdmin(NameAdmin):
    """
    Admin interface options for the SocialMedia model.
    Inherits common functionality from NameAdmin.
    """
    pass


@admin.register(Message)
class MessageAdmin(ReadOnlyAdmin):
    """
    Admin interface options for the Message model.
    Inherits common functionality from ReadOnlyAdmin.
    """

    def has_change_permission(self, request, obj=None):
        """
        Disable change functionality in the admin interface.
        """
        return False


@admin.register(AboutPage)
class AboutPageAdmin(NameAdmin):
    """
    Admin interface options for the AboutPage model.
    Inherits common functionality from NameAdmin.
    """
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Image model.
    """
    pass
