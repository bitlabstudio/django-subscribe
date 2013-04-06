"""Views of the ``subscribe`` app."""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from .forms import SubscriptionCreateForm, SubscriptionDeleteForm


class SubscriptionCreateView(FormView):
    """View that subscribes a ``User`` to any thing."""
    form_class = SubscriptionCreateForm
    template_name = 'subscribe/subscription_form.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user

        try:
            self.ctype = ContentType.objects.get(pk=kwargs.get('ctype_pk'))
        except ContentType.DoesNotExist:
            return Http404

        try:
            self.content_object = self.ctype.get_object_for_this_type(
                pk=kwargs.get('object_pk'))
        except ObjectDoesNotExist:
            return Http404

        return super(SubscriptionCreateView, self).dispatch(
            request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super(SubscriptionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(SubscriptionCreateView, self).get_context_data(**kwargs)
        ctx.update({
            'content_object': self.content_object,
        })
        return ctx

    def get_form_kwargs(self):
        kwargs = super(SubscriptionCreateView, self).get_form_kwargs()
        kwargs.update({
            'user': self.user,
            'content_object': self.content_object,
        })
        return kwargs

    def get_success_url(self):
        return self.content_object.get_absolute_url()


class SubscriptionDeleteView(SubscriptionCreateView):
    """View that un-subscribes a ``User`` from any thing."""
    form_class = SubscriptionDeleteForm
    template_name = 'subscribe/subscription_delete.html'
