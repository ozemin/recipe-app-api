"""
Django admin customization.
"""
from django.contrib import admin

from core import models

admin.site.register(models.User)
admin.site.register(models.Recipe)
admin.site.register(models.Tag)
