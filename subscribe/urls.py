"""URLs for the ``subscribe`` app."""
from django.conf.urls import url

from .views import SubscriptionCreateView, SubscriptionDeleteView


urlpatterns = [
    url(r'^create/(?P<ctype_pk>\d+)/(?P<object_pk>\d+)/$',
        SubscriptionCreateView.as_view(),
        name='subscriptions_create',),
    url(r'^delete/(?P<ctype_pk>\d+)/(?P<object_pk>\d+)/$',
        SubscriptionDeleteView.as_view(),
        name='subscriptions_delete',),
]
