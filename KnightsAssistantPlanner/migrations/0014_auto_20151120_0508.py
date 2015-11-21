# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0013_workouts_intensity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='workout',
        ),
        migrations.AddField(
            model_name='workouts',
            name='workout',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
