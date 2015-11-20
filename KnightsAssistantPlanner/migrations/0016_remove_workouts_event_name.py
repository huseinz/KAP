# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0015_workouts_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workouts',
            name='event_name',
        ),
    ]
