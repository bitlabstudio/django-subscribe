"""Tests for the models of the ``subscriptions`` app."""
from django.test import TestCase

from .factories import SubscriptionFactory


class SubscriptionTestCase(TestCase):
    """Tests for the ``Subscription`` model class."""
    def test_model(self):
        """Should be able to instantiate and save the model."""
        instance = SubscriptionFactory()
        self.assertTrue(instance.pk)
