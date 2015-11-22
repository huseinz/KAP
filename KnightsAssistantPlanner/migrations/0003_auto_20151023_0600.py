# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0002_auto_20151023_0546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='Year',
            new_name='year',
        ),
    ]
