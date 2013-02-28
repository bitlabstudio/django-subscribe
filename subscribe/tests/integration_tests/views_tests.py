"""Tests for the views of the ``subscriptions`` app."""
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from django_libs.tests.factories import UserFactory
from django_libs.tests.mixins import ViewTestMixin

from ..factories import DummyModelFactory, SubscriptionFactory


class SubscriptionCreateViewTestCase(ViewTestMixin, TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.dummy = DummyModelFactory()
        self.ctype = ContentType.objects.get_for_model(self.dummy)

    def get_view_name(self):
        return 'subscriptions_create'

    def get_view_kwargs(self):
        return {'ctype_pk': self.ctype.pk, 'object_pk': self.dummy.pk, }

    def test_anonymous(self):
        """Should redirect to login if user is anonymous."""
        self.should_redirect_to_login_when_anonymous()

    def test_callable(self):
        """Should be callable if user is authenticated."""
        self.should_be_callable_when_authenticated(self.user)


class SubscriptionDeleteViewTestCase(ViewTestMixin, TestCase):
    def setUp(self):
        self.subscription = SubscriptionFactory()
        self.ctype = ContentType.objects.get_for_model(
            self.subscription.content_type)

    def get_view_name(self):
        return 'subscriptions_delete'

    def get_view_kwargs(self):
        return {
            'ctype_pk': self.subscription.content_type.pk,
            'object_pk': self.subscription.object_id,
        }

    def test_anonymous(self):
        """Should redirect to login if user is anonymous."""
        self.should_redirect_to_login_when_anonymous()

    def test_callable(self):
        """Should be callable if user is authenticated."""
        self.should_be_callable_when_authenticated(self.subscription.user)
