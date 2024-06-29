from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration class for the 'home' app.

    Attributes:
        name (str): The name of the application.
        verbose_name (str): A human-readable name for the application, displayed in the Django admin interface.
    """
    name = 'home'
    verbose_name = "Home Management"
