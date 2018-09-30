"""
Hivemind URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [  # pylint: disable=invalid-name
    url(r'^admin/', admin.site.urls),
]
