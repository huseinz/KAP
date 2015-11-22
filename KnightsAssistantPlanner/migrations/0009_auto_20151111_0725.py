# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0008_workouts'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouts',
            name='day',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workouts',
            name='month',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workouts',
            name='year',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
