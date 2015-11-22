# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='year',
            new_name='Year',
        ),
    ]
