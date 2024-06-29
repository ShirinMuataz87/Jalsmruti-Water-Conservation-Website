"""
ASGI config for jalsmruti project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import environ
from django.core.asgi import get_asgi_application

# Initialize environment variables
env = environ.Env(
    DJANGO_SETTINGS_MODULE=(str, 'jalsmruti.settings')
)
# Read the .env file if it exists
environ.Env.read_env()

# Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))

# Get the ASGI application
application = get_asgi_application()
