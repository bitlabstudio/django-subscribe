"""Models for the ``subscribe`` app."""
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Subscription(models.Model):
    """
    Allows a ``User`` to subscribe to anything.

    :user: The ``User`` who subscribed to something.
    :content_object: Generic foreign key to the thing that the user is
      subscribed to.
    :date: Date when the subscription was created.

    """
    class Meta:
        unique_together = ('user', 'content_type', 'object_id', )

    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        related_name='subscriptions',
    )

    content_type = models.ForeignKey(
        ContentType,
        related_name='subscribed',
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation date'),
    )

    def __str__(self):
        return u'{0} subscribed to {1}'.format(
            self.user.email, self.content_object)
