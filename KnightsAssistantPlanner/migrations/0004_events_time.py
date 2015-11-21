# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0003_auto_20151023_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='time',
            field=models.CharField(max_length=5, null=True),
            preserve_default=True,
        ),
    ]
