"""Admin classes for the ``subscribe`` app."""
from django.contrib import admin

from .models import Subscription


admin.site.register(Subscription)
