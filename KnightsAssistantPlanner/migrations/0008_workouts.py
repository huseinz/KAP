# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0007_events_workout'),
    ]

    operations = [
        migrations.CreateModel(
            name='workouts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cal_count', models.IntegerField(default=15000)),
                ('large_muscle', models.CharField(max_length=10, choices=[(b'CHEST', b'Chest'), (b'THIGH', b'Thighs'), (b'UBACK', b'Upper back'), (b'LBACK', b'Lower back')])),
                ('small_muscle', models.CharField(max_length=10, choices=[(b'ABS', b'Abdominals'), (b'TRI', b'Triceps'), (b'BIC', b'Biceps'), (b'CAV', b'Calves')])),
                ('l_ex', models.CharField(max_length=10)),
                ('s_ex', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
