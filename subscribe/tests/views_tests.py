"""Tests for the views of the ``subscriptions`` app."""
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin
from mixer.backend.django import mixer

from .. import views


class SubscriptionCreateViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    view_class = views.SubscriptionCreateView

    def setUp(self):
        self.user = mixer.blend('auth.User')
        self.dummy = mixer.blend('test_app.DummyModel')
        self.ctype = ContentType.objects.get_for_model(self.dummy)

    def get_view_kwargs(self):
        return {'ctype_pk': self.ctype.pk, 'object_pk': self.dummy.pk, }

    def test_anonymous(self):
        """Should redirect to login if user is anonymous."""
        self.should_redirect_to_login_when_anonymous()

    def test_callable(self):
        """Should be callable if user is authenticated."""
        self.is_callable(user=self.user)


class SubscriptionDeleteViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    view_class = views.SubscriptionDeleteView

    def setUp(self):
        self.subscription = mixer.blend(
            'subscribe.Subscription',
            content_object=mixer.blend('test_app.DummyModel'))
        self.ctype = ContentType.objects.get_for_model(
            self.subscription.content_type)

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
        self.is_callable(user=self.subscription.user)
        self.is_postable(user=self.subscription.user, to='/')
