# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0004_events_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='time',
        ),
        migrations.AddField(
            model_name='events',
            name='hour',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='events',
            name='min',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
