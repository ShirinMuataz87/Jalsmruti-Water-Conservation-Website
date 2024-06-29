from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.exceptions import Throttled


class ContactFormRateThrottleMixin:
    """
    Mixin to apply rate throttling for contact form submissions.

    This mixin uses Django REST Framework's AnonRateThrottle and UserRateThrottle
    to limit the rate of form submissions. It raises a Throttled exception if the
    rate limit is exceeded.

    Attributes:
        throttle_classes (list): List of throttle classes to be applied.

    Methods:
        throttled(request, wait):
            Raises a Throttled exception with a custom message and wait time.
    """
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def throttled(self, request, wait):
        """
        Handle throttling by raising a Throttled exception with a custom message.

        Args:
            request: The HTTP request object.
            wait (int): The number of seconds to wait before the next allowed request.

        Raises:
            Throttled: Exception with a custom detail message and wait time.
        """
        raise Throttled(detail={
            'message': 'Too many requests, please try again later.',
            'available_in': f'{wait} seconds'
        })