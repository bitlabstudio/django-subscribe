"""Factories for the ``subscriptions`` app."""
from django.contrib.contenttypes.models import ContentType

import factory

from django_libs.tests.factories import UserFactory

from ..models import Subscription
from .test_app.models import DummyModel


class DummyModelFactory(factory.Factory):
    """Factory for ``DummyModel`` objects."""
    FACTORY_FOR = DummyModel

    name = 'Test name'


class SubscriptionFactory(factory.Factory):
    """
    Factory for ``Subscription`` objects.

    You can call it with ``SubscriptionFactory(content_object=yourobject)``.
    If you don't pass in the ``content_object`` kwarg, it will create a
    ``DummyObject`` to subscribe to.

    """

    FACTORY_FOR = Subscription

    user = factory.SubFactory(UserFactory)

    @classmethod
    def _prepare(cls, create, **kwargs):
        """Creates a new ``DummyModel`` if no ``content_object`` provided."""
        content_object = kwargs.pop('content_object', None)
        subscription = super(SubscriptionFactory, cls)._prepare(
            False, **kwargs)
        if not content_object:
            content_object = DummyModelFactory()
        subscription.content_type = ContentType.objects.get_for_model(
            content_object)
        subscription.object_id = content_object.pk
        if create:
            subscription.save()
        return subscription
