# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0005_auto_20151028_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='notes',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
