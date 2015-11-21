# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0010_events_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='user',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
