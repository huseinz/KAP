# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=40)),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('year', models.IntegerField()),
                ('hour', models.IntegerField(null=True)),
                ('min', models.IntegerField(null=True)),
                ('notes', models.CharField(max_length=200, null=True)),
                ('user', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='workouts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cal_count', models.IntegerField(default=15000)),
                ('large_muscle', models.CharField(max_length=10, choices=[(b'CHEST', b'Chest'), (b'THIGH', b'Thighs'), (b'UBACK', b'Upper back'), (b'LBACK', b'Lower back')])),
                ('small_muscle', models.CharField(max_length=10, choices=[(b'ABS', b'Abdominals'), (b'TRI', b'Triceps'), (b'BIC', b'Biceps'), (b'CAV', b'Calves')])),
                ('l_ex', models.CharField(max_length=10)),
                ('s_ex', models.CharField(max_length=10)),
                ('month', models.IntegerField(null=True)),
                ('day', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('user', models.CharField(max_length=30, null=True)),
                ('intensity', models.CharField(max_length=10, null=True, choices=[(b'LIT', b'Light'), (b'MED', b'Medium'), (b'HRD', b'Hard')])),
                ('workout', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='workouts',
            unique_together=set([('month', 'day', 'year')]),
        ),
    ]
