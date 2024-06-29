#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""
import os
import sys
import environ


def main():
    """
    Set the default Django settings module and execute the command line utility.
    """
    env = environ.Env(
        DJANGO_SETTINGS_MODULE=(str, 'jalsmruti.settings')
    )
    # Read the .env file if it exists
    environ.Env.read_env()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment variable."
            " Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
