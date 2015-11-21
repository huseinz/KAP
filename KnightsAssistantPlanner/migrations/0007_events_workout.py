# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0006_events_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='workout',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
