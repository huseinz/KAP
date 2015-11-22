# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0014_auto_20151120_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouts',
            name='event_name',
            field=models.CharField(max_length=40, null=True),
            preserve_default=True,
        ),
    ]
