"""Forms for the ``subscribe`` app."""
from django import forms
from django.contrib.contenttypes.models import ContentType

from .models import Subscription


class SubscriptionCreateForm(forms.Form):
    def __init__(self, user, content_object, *args, **kwargs):
        self.user = user
        self.content_object = content_object
        self.ctype = ContentType.objects.get_for_model(self.content_object)
        super(SubscriptionCreateForm, self).__init__(*args, **kwargs)

    def _get_method_kwargs(self):
        """
        Helper method. Returns kwargs needed to filter the correct object.

        Can also be used to create the correct object.

        """
        method_kwargs = {
            'user': self.user,
            'content_type': self.ctype,
            'object_id': self.content_object.pk,
        }
        return method_kwargs

    def save(self, *args, **kwargs):
        """Adds a subscription for the given user to the given object."""
        method_kwargs = self._get_method_kwargs()
        try:
            subscription = Subscription.objects.get(**method_kwargs)
        except Subscription.DoesNotExist:
            subscription = Subscription.objects.create(**method_kwargs)
        return subscription


class SubscriptionDeleteForm(SubscriptionCreateForm):
    def save(self, *args, **kwargs):
        """Removes a subscription for the given user from the given object."""
        method_kwargs = self._get_method_kwargs()
        try:
            subscription = Subscription.objects.get(**method_kwargs)
        except Subscription.DoesNotExist:
            return
        subscription.delete()
