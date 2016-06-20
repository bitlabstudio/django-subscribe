"""Tests for the models of the ``subscriptions`` app."""
from django.test import TestCase

from mixer.backend.django import mixer


class SubscriptionTestCase(TestCase):
    """Tests for the ``Subscription`` model class."""
    def test_model(self):
        """Should be able to instantiate and save the model."""
        instance = mixer.blend('subscribe.Subscription')
        self.assertTrue(str(instance))
