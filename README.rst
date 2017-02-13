Django Subscribe
================

A simple subscription app for Django.


Installation
------------

Prerequisites:

* Django

If you want to install the latest stable release from PyPi::

    $ pip install django-subscribe

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-subscribe.git#egg=subscribe

Add ``subscribe`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'subscribe',
    )

Run the South migrations::

    ./manage.py migrate subscribe


Usage
-----

In order to render a subscribe/unsubscribe button next to an object, do this::

    {% load i18n subscribe_tags %}
    {% get_subscribers object as subscribers %}
    {% get_ctype object as ctype %}
    {% is_subscribed user object as user_is_subscribed %}
    {% if user_is_subscribed %}
        <p><a href="{% url "subscriptions_delete" ctype_pk=ctype.pk object_pk=object.pk %}">{% trans "Un-subscribe" %}</a></p>
    {% else %}
        <p><a href="{% url "subscriptions_create" ctype_pk=ctype.pk object_pk=object.pk %}">{% trans "Subscribe" %}</a></p>
    {% endif %}

Test
----

For a test run

    $ python manage.py check
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver

and check it out at http://localhost:8000/admin


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
