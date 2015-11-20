# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0016_remove_workouts_event_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='workouts',
            unique_together=set([('month', 'day', 'year')]),
        ),
    ]
