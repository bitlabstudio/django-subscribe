# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('content_type', models.ForeignKey(related_name='subscribed', to='contenttypes.ContentType')),
                ('user', models.ForeignKey(related_name='subscriptions', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('user', 'content_type', 'object_id')]),
        ),
    ]
