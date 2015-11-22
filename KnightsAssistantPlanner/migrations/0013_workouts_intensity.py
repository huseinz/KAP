# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0012_workouts_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouts',
            name='intensity',
            field=models.CharField(max_length=10, null=True, choices=[(b'LIT', b'Light'), (b'MED', b'Medium'), (b'HRD', b'Hard')]),
            preserve_default=True,
        ),
    ]
