"""
App Configuration for the API Module
"""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    App Config for Api Module
    """
    name = 'api'

    def ready(self):
        # pylint: disable=unused-variable
        import signals  # noqa
