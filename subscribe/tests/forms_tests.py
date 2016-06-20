"""Tests for the forms of the ``subscriptions`` app."""
from django.test import TestCase

from mixer.backend.django import mixer

from ..forms import SubscriptionCreateForm, SubscriptionDeleteForm
from ..models import Subscription


class SubscriptionCreateFormTestCase(TestCase):
    """Tests for the ``SubscriptionCreateForm`` form class."""
    longMessage = True

    def test_save(self):
        """Should create a new subscription."""
        user = mixer.blend('auth.User')
        dummy = mixer.blend('test_app.DummyModel')
        form = SubscriptionCreateForm(user=user, content_object=dummy, data={})
        self.assertTrue(form.is_valid(), msg=(
            'Errors: {0}'.format(form.errors.items())))
        instance = form.save()
        self.assertTrue(instance.pk)


class SubscriptionDeleteFormTestCase(TestCase):
    """Tests for the ``SubscriptionDeleteForm`` form class."""
    longMessage = True

    def test_save(self):
        """Should delete the subscription."""
        sub = mixer.blend('subscribe.Subscription',
                          content_object=mixer.blend('test_app.DummyModel'))
        form = SubscriptionDeleteForm(
            user=sub.user, content_object=sub.content_object, data={})
        self.assertTrue(form.is_valid(), msg=(
            'Errors: {0}'.format(form.errors.items())))
        form.save()
        self.assertEqual(Subscription.objects.all().count(), 0)

    def test_no_subscription(self):
        """
        Should fail graciously if trying to delete a non existant subscription.

        """
        sub = mixer.blend('subscribe.Subscription',
                          content_object=mixer.blend('test_app.DummyModel'))
        form = SubscriptionDeleteForm(
            user=sub.user, content_object=sub.content_object, data={})
        self.assertTrue(form.is_valid(), msg=(
            'Errors: {0}'.format(form.errors.items())))
        sub.delete()
        form.save()
        self.assertEqual(Subscription.objects.all().count(), 0)
