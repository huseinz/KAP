# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0017_auto_20151120_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouts',
            name='cal_count',
            field=models.IntegerField(default=15000, null=True),
        ),
        migrations.AlterField(
            model_name='workouts',
            name='large_muscle',
            field=models.CharField(max_length=10, null=True, choices=[(b'CHEST', b'Chest'), (b'THIGH', b'Thighs'), (b'UBACK', b'Upper back'), (b'LBACK', b'Lower back')]),
        ),
        migrations.AlterField(
            model_name='workouts',
            name='small_muscle',
            field=models.CharField(max_length=10, null=True, choices=[(b'ABS', b'Abdominals'), (b'TRI', b'Triceps'), (b'BIC', b'Biceps'), (b'CAV', b'Calves')]),
        ),
    ]
