from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date(date):
    """
    Validate that the provided date is not in the past.

    Args:
        date (datetime.date): The date to validate.

    Raises:
        ValidationError: If the date is in the past.
    """
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past.")
