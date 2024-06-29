from django.contrib import admin


class ReadOnlyAdmin(admin.ModelAdmin):
    """
    Base admin class to make certain fields read-only and disable add/delete functionality.
    """

    def has_add_permission(self, request):
        """
        Disable add functionality.

        Args:
            request (HttpRequest): The request object.

        Returns:
            bool: Always returns False to disable adding new records.
        """
        return False


class UrlSlugAdmin(admin.ModelAdmin):
    """
    Base admin class to make the url_slug field read-only.

    Attributes:
        readonly_fields (tuple): Fields to make read-only in the admin interface.
    """
    readonly_fields = ("url_slug",)


class NameAdmin(admin.ModelAdmin):
    """
    Base admin class to make the name field read-only and disable add/delete functionality.

    Attributes:
        exclude (tuple): Fields to exclude in the admin interface.
        readonly_fields (tuple): Fields to make read-only in the admin interface.
    """
    exclude = ("name",)
    readonly_fields = ("name",)

    def has_add_permission(self, request):
        """
        Disable add functionality.

        Args:
            request (HttpRequest): The request object.

        Returns:
            bool: Always returns False to disable adding new records.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Disable delete functionality.

        Args:
            request (HttpRequest): The request object.
            obj (Model): The object being deleted.

        Returns:
            bool: Always returns False to disable deleting records.
        """
        return False
