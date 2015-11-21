# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0011_auto_20151119_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouts',
            name='user',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
