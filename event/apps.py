from django.apps import AppConfig


class EventConfig(AppConfig):
    """
    Configuration class for the 'event' app.

    Attributes:
        name (str): The name of the application.
        verbose_name (str): A human-readable name for the application, displayed in the Django admin interface.
    """
    name = 'event'
    verbose_name = "Event Management"
