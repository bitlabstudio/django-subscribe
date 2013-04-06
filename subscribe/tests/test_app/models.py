"""Dummy models for tests of the ``subscription`` app."""
from django.db import models


class DummyModel(models.Model):
    name = models.CharField(max_length=256)

    def get_absolute_url(self):
        return '/'
